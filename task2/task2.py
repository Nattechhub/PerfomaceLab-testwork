import sys
import math


def check_points(circle_file, points_file):
    # Читаем данные из файла с центром окружности и радиусом
    with open(circle_file, 'r') as f:
        circle_data = f.readlines()

    # Читаем данные из файла с точками
    with open(points_file, 'r') as f:
        points_data = f.readlines()

    # Парсим координаты центра окружности и радиус
    circle_x, circle_y = map(float, circle_data[0].strip().split())
    radius = float(circle_data[1].strip())

    results = []
    for point in points_data:
        # Парсим координаты точки
        point_x, point_y = map(float, point.strip().split())

        # Вычисляем расстояние от точки до центра окружности
        distance = math.sqrt((point_x - circle_x) ** 2 + (point_y - circle_y) ** 2)

        # Определяем положение точки относительно окружности
        if distance < radius:
            results.append(1)
        elif distance == radius:
            results.append(0)
        else:
            results.append(2)

    # Выводим результаты для каждой точки
    for result in results:
        print(result)


if __name__ == "__main__":
    # Проверяем, что переданы два аргумента командной строки
    if len(sys.argv) < 3:
        print("Для запуска, используйте команду: python task2.py circle.txt points.txt")
    else:
        # Получаем пути к файлам из аргументов командной строки
        circle_file = sys.argv[1]
        points_file = sys.argv[2]

        # Вызываем функцию для проверки точек
        check_points(circle_file, points_file)
