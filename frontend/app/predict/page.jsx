'use client';

import { useState } from 'react';

export default function PredictPage() {
  const [formData, setFormData] = useState({
    Hours_Studied_Per_Day: '',
    Total_Study_Days: '',
    Past_Percentage: '',
    Attendance_Percentage: '',
    Parental_Support: 'Yes',
    Internet_Access: 'Yes',
    School_Type: 'Private',
    Sleep_Hours: '',
    Social_Media_Hours: '',
    Coaching: 'Yes',
    Gender: 'Male',
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setError(null);
    try {
      const response = await fetch('https://students-percentage-predictor.onrender.com/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      if (response.ok) {
        setResult(data.prediction);
      } else {
        setError(data.error || 'Something went wrong.');
      }
    } catch (err) {
      setError('Server error. Please try again later.');
    }
  };

  return (
    <div className="container">
      <h2>📈 Predict Your Exam Score</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map(key => (
          <div key={key}>
            <label>{key.replace(/_/g, ' ')}</label>
            {['Parental_Support', 'Internet_Access', 'School_Type', 'Coaching', 'Gender'].includes(key) ? (
              <select name={key} value={formData[key]} onChange={handleChange}>
                {key === 'Gender'
                  ? <>
                      <option value="Male">Male</option>
                      <option value="Female">Female</option>
                    </>
                  : key === 'School_Type'
                  ? <>
                      <option value="Private">Private</option>
                      <option value="Govt">Govt</option>
                    </>
                  : <>
                      <option value="Yes">Yes</option>
                      <option value="No">No</option>
                    </>
                }
              </select>
            ) : (
              <input
                type="number"
                step="0.1"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                required
              />
            )}
          </div>
        ))}

        <button type="submit">Predict</button>
      </form>

      {result && <div className="result">🎯 Predicted Score: {result}%</div>}
      {error && <div className="result" style={{ color: 'red' }}>{error}</div>}
    </div>
  );
}
