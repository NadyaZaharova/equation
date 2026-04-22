import tkinter as tk
from tkinter import ttk, messagebox
import math


class QuadraticSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Решение квадратного уравнения")
        self.root.geometry("550x500")
        self.root.resizable(False, False)

        # Настройка стиля
        self.root.configure(bg='#f0f0f0')

        # Заголовок
        title_label = tk.Label(
            root,
            text="Квадратное уравнение ax² + bx + c = 0",
            font=("Arial", 14, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=10)

        # Рамка для ввода коэффициентов
        input_frame = tk.Frame(root, bg='#f0f0f0', relief=tk.GROOVE, bd=2)
        input_frame.pack(pady=20, padx=20, fill='x')

        # Коэффициент a
        tk.Label(
            input_frame,
            text="Коэффициент a:",
            font=("Arial", 11),
            bg='#f0f0f0'
        ).grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.a_entry = tk.Entry(
            input_frame,
            font=("Arial", 11),
            width=20,
            relief=tk.SUNKEN,
            bd=2
        )
        self.a_entry.grid(row=0, column=1, padx=10, pady=10)
        self.a_entry.insert(0, "1")

        # Коэффициент b
        tk.Label(
            input_frame,
            text="Коэффициент b:",
            font=("Arial", 11),
            bg='#f0f0f0'
        ).grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.b_entry = tk.Entry(
            input_frame,
            font=("Arial", 11),
            width=20,
            relief=tk.SUNKEN,
            bd=2
        )
        self.b_entry.grid(row=1, column=1, padx=10, pady=10)
        self.b_entry.insert(0, "0")

        # Коэффициент c
        tk.Label(
            input_frame,
            text="Коэффициент c:",
            font=("Arial", 11),
            bg='#f0f0f0'
        ).grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.c_entry = tk.Entry(
            input_frame,
            font=("Arial", 11),
            width=20,
            relief=tk.SUNKEN,
            bd=2
        )
        self.c_entry.grid(row=2, column=1, padx=10, pady=10)
        self.c_entry.insert(0, "0")

        # Кнопки
        button_frame = tk.Frame(root, bg='#f0f0f0')
        button_frame.pack(pady=20)

        self.solve_button = tk.Button(
            button_frame,
            text="Решить уравнение",
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=8,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.solve_equation
        )
        self.solve_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(
            button_frame,
            text="Очистить",
            font=("Arial", 11, "bold"),
            bg='#f44336',
            fg='white',
            padx=20,
            pady=8,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.clear_fields
        )
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # Рамка для результата
        result_frame = tk.Frame(root, bg='#f0f0f0', relief=tk.GROOVE, bd=2)
        result_frame.pack(pady=10, padx=20, fill='both', expand=True)

        tk.Label(
            result_frame,
            text="Результат:",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0'
        ).pack(anchor='w', padx=10, pady=5)

        # Текстовое поле для вывода результата
        self.result_text = tk.Text(
            result_frame,
            font=("Courier New", 11),
            height=12,
            width=60,
            relief=tk.SUNKEN,
            bd=2,
            bg='white',
            fg='#333333'
        )
        self.result_text.pack(padx=10, pady=10, fill='both', expand=True)

        # Скроллбар для текстового поля
        scrollbar = tk.Scrollbar(self.result_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

        # Статус бар
        self.status_bar = tk.Label(
            root,
            text="Готов к работе",
            font=("Arial", 9),
            bg='#e0e0e0',
            relief=tk.SUNKEN,
            anchor='w'
        )
        self.status_bar.pack(side=tk.BOTTOM, fill='x')

        # Привязка клавиши Enter к решению
        self.root.bind('<Return>', lambda event: self.solve_equation())

    def solve_equation(self):
        """Решение квадратного уравнения"""
        try:
            # Получаем значения
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

            # Проверка на a = 0
            if a == 0:
                messagebox.showerror(
                    "Ошибка",
                    "Коэффициент a не может быть равен 0!\nЭто не квадратное уравнение."
                )
                self.status_bar.config(text="Ошибка: a = 0")
                return

            # Очищаем поле результата
            self.result_text.delete(1.0, tk.END)

            # Вывод уравнения
            self.result_text.insert(tk.END, "=" * 50 + "\n")
            self.result_text.insert(tk.END, "РЕШЕНИЕ КВАДРАТНОГО УРАВНЕНИЯ\n")
            self.result_text.insert(tk.END, "=" * 50 + "\n\n")

            # Формируем уравнение
            equation_str = f"Уравнение: {a}x² + {b}x + {c} = 0\n"
            self.result_text.insert(tk.END, equation_str)
            self.result_text.insert(tk.END, "-" * 40 + "\n\n")

            # Вычисление дискриминанта
            D = b ** 2 - 4 * a * c

            self.result_text.insert(tk.END, "Ход решения:\n")
            self.result_text.insert(tk.END, f"1. Находим дискриминант:\n")
            self.result_text.insert(tk.END, f"   D = b² - 4ac\n")
            self.result_text.insert(tk.END, f"   D = ({b})² - 4·{a}·{c}\n")
            self.result_text.insert(tk.END, f"   D = {b ** 2} - {4 * a * c}\n")
            self.result_text.insert(tk.END, f"   D = {D}\n\n")

            if D < 0:
                self.result_text.insert(tk.END, "2. Анализ дискриминанта:\n")
                self.result_text.insert(tk.END, f"   D = {D} < 0\n\n")
                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, "❌ РЕЗУЛЬТАТ: Корней нет\n")
                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, "Дискриминант отрицательный,\n")
                self.result_text.insert(tk.END, "уравнение не имеет действительных корней.\n")
                self.status_bar.config(text="Корней нет")

            elif D == 0:
                x = (-b + math.sqrt(D)) / (2 * a)

                self.result_text.insert(tk.END, "2. Анализ дискриминанта:\n")
                self.result_text.insert(tk.END, f"   D = {D} = 0\n\n")
                self.result_text.insert(tk.END, "3. Находим корень:\n")
                self.result_text.insert(tk.END, f"   x = -b/(2a)\n")
                self.result_text.insert(tk.END, f"   x = -({b})/(2·{a})\n")
                self.result_text.insert(tk.END, f"   x = {-b}/{2 * a}\n\n")

                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, "✅ РЕЗУЛЬТАТ: Один корень\n")
                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, f"x = {x}\n")
                self.status_bar.config(text=f"Найден один корень: {x}")

            else:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)

                self.result_text.insert(tk.END, "2. Анализ дискриминанта:\n")
                self.result_text.insert(tk.END, f"   D = {D} > 0\n\n")
                self.result_text.insert(tk.END, "3. Находим корни:\n")
                self.result_text.insert(tk.END, f"   x₁ = (-b + √D)/(2a)\n")
                self.result_text.insert(tk.END, f"   x₁ = ({-b} + √{D})/(2·{a})\n")
                self.result_text.insert(tk.END, f"   x₁ = ({-b + math.sqrt(D)})/{2 * a}\n")
                self.result_text.insert(tk.END, f"   x₁ = {x1}\n\n")

                self.result_text.insert(tk.END, f"   x₂ = (-b - √D)/(2a)\n")
                self.result_text.insert(tk.END, f"   x₂ = ({-b} - √{D})/(2·{a})\n")
                self.result_text.insert(tk.END, f"   x₂ = ({-b - math.sqrt(D)})/{2 * a}\n")
                self.result_text.insert(tk.END, f"   x₂ = {x2}\n\n")

                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, "✅ РЕЗУЛЬТАТ: Два корня\n")
                self.result_text.insert(tk.END, "=" * 40 + "\n")
                self.result_text.insert(tk.END, f"x₁ = {x1}\n")
                self.result_text.insert(tk.END, f"x₂ = {x2}\n")
                self.status_bar.config(text=f"Найдено два корня: {x1:.2f} и {x2:.2f}")

            # Прокрутка вверх
            self.result_text.see(1.0)

        except ValueError:
            messagebox.showerror(
                "Ошибка ввода",
                "Пожалуйста, введите корректные числовые значения для всех коэффициентов."
            )
            self.status_bar.config(text="Ошибка: некорректный ввод")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{str(e)}")
            self.status_bar.config(text=f"Ошибка: {str(e)}")

    def clear_fields(self):
        """Очистка всех полей ввода и результата"""
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)

        self.a_entry.insert(0, "1")
        self.b_entry.insert(0, "0")
        self.c_entry.insert(0, "0")

        self.result_text.delete(1.0, tk.END)
        self.status_bar.config(text="Поля очищены")


def main():
    root = tk.Tk()
    app = QuadraticSolver(root)
    root.mainloop()


if __name__ == "__main__":
    main()