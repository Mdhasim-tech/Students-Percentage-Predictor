# 🎓 Student Percentage Predictor

A full-stack Machine Learning web application that predicts a student's percentage based on study-related inputs. The project combines a **K-Nearest Neighbors (KNN)** regression model with a modern **Next.js** frontend and a **Flask** backend to provide real-time predictions through an intuitive web interface.

---

## 📸 Demo

<img width="1362" height="675" alt="study1" src="https://github.com/user-attachments/assets/00a4fb10-697d-41f0-b7f9-caac17fe16cd" />
<img width="1349" height="677" alt="study3" src="https://github.com/user-attachments/assets/afeeacac-fd5d-42e9-af5f-131ff7829930" />
<img width="1349" height="677" alt="study2" src="https://github.com/user-attachments/assets/c1eab895-dcff-4254-beb0-cb62e9ff5521" />


---

## 🚀 Features

- Predicts student percentage using Machine Learning.
- Clean and responsive user interface.
- Real-time prediction through REST API.
- Trained using the K-Nearest Neighbors (KNN) algorithm.
- Full-stack architecture with separate frontend and backend.
- Easy to deploy and extend.

---

## 🛠️ Tech Stack

### Frontend
- Next.js
- React.js
- CSS

### Backend
- Flask
- Python
- scikit-learn
- Pandas
- NumPy

### Machine Learning
- K-Nearest Neighbors (KNN) Regressor

---

## 📂 Project Structure

```
Students-Percentage-Predictor/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── ...
│
├── backend/
│   ├── app.py
│   ├── knn_regressor1.py
│   ├── student_knn_model.pkl
│   ├── student_performance_dataset.csv
│   └── requirements.txt

```

---

## ⚙️ How It Works

1. User enters study-related information.
2. The frontend sends the data to the Flask API.
3. The trained KNN model processes the input.
4. The predicted student percentage is returned.
5. The frontend displays the prediction instantly.

---

## 📊 Machine Learning Model

**Algorithm:** K-Nearest Neighbors (KNN) Regressor

### Dataset Features

- Study Hours
- Previous Scores
- Sleep Hours
- Sample Question Papers Practiced
- Attendance
- Other academic factors

**Target Variable**

- Student Percentage

---

## 🖥️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Students-Percentage-Predictor.git

cd Students-Percentage-Predictor
```

---

# Backend Setup

```bash
cd backend

pip install -r requirements.txt

python app.py
```

Runs on:

```
http://127.0.0.1:5000
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Runs on:

```
http://localhost:3000
```

---

## 🔗 API

### POST `/predict`

Predicts the student's percentage.

### Request

```json
{
  "study_hours": 6,
  "attendance": 90,
  "previous_score": 82,
  "sleep_hours": 7,
  "sample_papers": 8
}
```

### Response

```json
{
  "predicted_percentage": 87.43
}
```

---

## 📈 Future Improvements

- Support multiple ML models
- Compare model accuracies
- User authentication
- Save prediction history
- Deploy frontend and backend
- Interactive charts and analytics

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Md Hasim**

GitHub: https://github.com/Mdhasim-tech<img width="1362" height="675" alt="study1" src="https://github.com/user-attachments/assets/082ed43b-78af-4405-a3b8-1e5176d8b210" />
<img width="1349" height="677" alt="study3" src="https://github.com/user-attachments/assets/ed173bdc-7dab-4002-885f-c5e0f6eebbb6" />
<img width="1349" height="677" alt="study2" src="https://github.com/user-attachments/assets/7df70c6e-4bc3-4bec-852b-0ea7a1d24691" />
