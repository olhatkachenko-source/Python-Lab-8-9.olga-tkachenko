import nltk
from nltk.corpus import *
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import matplotlib.pyplot as plt

# Завантаження необхідних ресурсів NLTK (якщо вони ще не завантажені)
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

#  Завантаження тексту відповідно до 19 варіанта
text_name = 'carroll-alice.txt'
alice_words = nltk.corpus.gutenberg.words(text_name)

print(f"=== АНАЛІЗ ТЕКСТУ: {text_name} (ВАРІАНТ 19) ===\n")

# Визначення загальної кількості слів та кількості унікальних слів
total_words = len(alice_words)
unique_words = len(set(alice_words))

print(f"Загальна кількість слів у тексті: {total_words}")
print(f"Кількість унікальних слів у тексті: {unique_words}")

# Визначення 10 найбільш уживаних слів у тексті та побудова стовпчастої діаграми
fdist = FreqDist(alice_words)
top_ten_raw = fdist.most_common(10)

print("\n10 найбільш уживаних слів у початковому тексті:")
for word, freq in top_ten_raw:
    print(f"  - {word}: {freq} разів")

# Побудова стовпчастої діаграми для первинного тексту
words_raw, counts_raw = zip(*top_ten_raw)
plt.figure(figsize=(10, 5))
plt.bar(words_raw, counts_raw, color='skyblue')
plt.title(f'Top 10 most common words in {text_name} (Raw)', fontsize=14)
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, axis='y')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words("english"))

# Видалення стоп-слів, переведення у нижній регістр та видалення пунктуації
table = str.maketrans('', '', string.punctuation)
cleaned_words = [
    word.translate(table).lower() 
    for word in alice_words 
    if word.lower() not in stop_words
]

# Видалення порожніх елементів і залишення лише буквених слів (isalpha)
cleaned_words = [word for word in cleaned_words if word and word.isalpha()]

# Визначення 10 найбільш уживаних слів після очищення та побудова діаграми
fdist_cleaned = FreqDist(cleaned_words)
top_ten_cleaned = fdist_cleaned.most_common(10)

print("\n10 найбільш уживаних слів після видалення стоп-слів та пунктуації:")
for word, freq in top_ten_cleaned:
    print(f"  - {word}: {freq} разів")

# Побудова стовпчастої діаграми для очищеного тексту
words_clean, counts_clean = zip(*top_ten_cleaned)
plt.figure(figsize=(10, 5))
plt.bar(words_clean, counts_clean, color='coral')
plt.title(f'Top 10 most common words in {text_name} (Without Stopwords & Punctuation)', fontsize=14)
plt.xlabel('Words', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, axis='y')
plt.show()

# Виконання стемінгу (PorterStemmer) та визначення топ-10 після обробки
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in cleaned_words]

fdist_stemmed = FreqDist(stemmed_words)
top_ten_stemmed = fdist_stemmed.most_common(10)

print("\n10 найбільш уживаних слів після стемінгу (PorterStemmer):")
for word, freq in top_ten_stemmed:
    print(f"  - {word}: {freq} разів")
