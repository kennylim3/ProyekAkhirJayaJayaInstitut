# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus. Sebagai calon data scientist masa depan, Anda diminta untuk membantu Jaya Jaya Institut dalam menyelesaikan permasalahannya. Mereka juga meminta Anda untuk membuatkan dashboard agar mereka mudah dalam memahami data dan memonitor performa siswa. 

### Permasalahan Bisnis
Hingga saat ini, Jaya Jaya Institut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
Untuk penyelesaian masalah Jaya Jaya Institut, akan dibuat dashboard untuk memudahkan pemantauan performa siswa. Selain itu juga akan dikembangkan sebuah sistem machine learning dengan mencoba 3 algoritma, yaitu decision tree, random forest, dan gradient booster, yang akan dibandingkan hasilnya untuk mendapatkan model yang memiliki performa paling baik. Machine learning yang telah dibuat akan diimplementasikan pada sebuah prototipe sederhana untuk memprediksi siswa yang memiliki peluang dropout yang tinggi.

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

Setup environment:
```
pipenv install
pipenv shell
pip install pandas matplotlib seaborn sqlalchemy scikit-learn joblib numpy streamlit
```

## Business Dashboard
Dashboard yang telah dibuat memuat visualisasi dari informasi-informasi berupa jumlah dan persentase siswa, persebaran usia siswa, serta grafik performa siswa pada semester 1 dan 2.

## Menjalankan Sistem Machine Learning
Input data-data yang diminta, kemudian klik tombol predict. 

```

```

## Conclusion
- Siswa yang dropout cenderung memiliki Admission_grade lebih rendah, berumur lebih tua, Curricular_units_1st_sem_enrolled lebih sedikit, Curricular_units_1st_sem_approved lebih sedikit, Curricular_units_1st_sem_grade lebih rendah, Curicular_units_2nd_sem_enrolled lebih sedikit, Curricular_units_2nd_sem_approved lebih sedikit, dan Curricular_units_2nd_sem_grade lebih rendah.
- Tidak terdapat pola menarik pada feature Application_order, Previous_qualification_grade, Curricular_units_1st_sem_credited, Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_without_evaluations, Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_evaluations, dan Curricular_units_2nd_sem_without_evaluations.
- Siswa yang lulus/graduate cenderung displaced, sedangkan yang dropout tidak displaced.
- Tidak ditemukan pola menarik pada feature Marital_status, Application_mode, Course, Daytime_evening_attendance, Previous_qualification, Nationality, Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation, Educational_special_needs, Debtor, Tuition_fees_up_to_date, Gender, Scholarship_holder, dan International.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Lakukan intervensi pada siswa-siswa dengan nilai-nilai rendah, lakukan program bimbingan atau dukungan tambahan untuk membantu siswa dengan nilai rendah meningkatkan performa akademik mereka.
- Perhatikan siswa-siswa yang berumur lebih tua dan berikan dukungan yang sekiranya dibutuhkan.
