import math
import matplotlib.pyplot as plt


def analyze_coordinates(point):
    """Analyzes the coordinates of a point and determines its position"""
    result = ""
    quadrant = ""

    match point:
        case [0, 0]:
            result = "Origin"
            quadrant = "Origin"
        case [0, y]:
            result = f"On the Y-axis at y = {y}"
            quadrant = "Y-axis"
        case [x, 0]:
            result = f"On the X-axis at x = {x}"
            quadrant = "X-axis"
        case [x, y] if x > 0 and y > 0:
            distance = math.sqrt(x**2 + y**2)   # відстань від початку координат до точки sqrt((0-x)**2 + (0-12)**2)
            angle = math.degrees(math.atan2(y, x))  #atan2() у радіанах, degrees() перетворить у градуси
            result = f"Point ({x}, {y}) in I quadrant\nDistance from the origin to the point: {distance:.2f}\nThe angle between the X-axis: {angle:.2f}°"
            quadrant = "I"
        case [x, y] if x < 0 and y > 0:
            distance = math.sqrt(x**2 + y**2)
            angle = math.degrees(math.atan2(y, x))
            result = f"Point ({x}, {y}) in II quadrant\nDistance from the origin to the point: {distance:.2f}\nThe angle between the X-axis: {angle:.2f}°"
            quadrant = "II"
        case [x, y] if x < 0 and y < 0:
            distance = math.sqrt(x**2 + y**2)
            angle = math.degrees(math.atan2(y, x))
            result = f"Point ({x}, {y}) in III quadrant\nDistance from the origin to the point: {distance:.2f}\nThe angle between the X-axis: {angle:.2f}°"
            quadrant = "III"
        case [x, y] if x > 0 and y < 0:
            distance = math.sqrt(x ** 2 + y ** 2)
            angle = math.degrees(math.atan2(y, x))
            result = f"Point ({x}, {y}) in IV quadrant\nDistance from the origin to the point: {distance:.2f}\nThe angle between the X-axis: {angle:.2f}°"
            quadrant = "IV"
        case _:
            result = f"Incorrect point {point}"
            quadrant = None
    print(result)
    return quadrant, point if len(point) == 2 else None # повернути point тільки якщо вона має [x, y]


def visualize_points(points):
    """Visualizes points on the coordinate plane"""

    fig, ax = plt.subplots(figsize=(10, 10))

    # Осі координат
    ax.axhline(y=0, color='k', linewidth=0.8) # Вісь X
    ax.axvline(x=0, color='k', linewidth=0.8) # Вісь Y
    ax.grid(True, alpha=0.3)

    # кольори для різних чвертей
    colors = {
        "I": "blue",
        "II": "green",
        "III": "red",
        "IV": "orange",
        "Origin": "black",
        "X-axis": "purple",
        "Y-axis": "brown"
    }

    # Обробка точок
    for point in points:
        quadrant, coords = analyze_coordinates(point) # витягує наприклад "II", [-2, 3]
        print('-' * 50)

        if coords: # Якщо точка НЕ None, то малюємо її
            x, y = coords
            # quadrant ми витягнули з analyze_coordinates(point)
            color = colors.get(quadrant, 'gray') # .get(ключ, значення_за_замовчуванням)
            ax.plot(x, y, 'o', markersize=12, color=color, label=f"{point} ({quadrant})")
            ax.text(x + 0.2, y + 0.2, f'({x}, {y})', fontsize=15) # простіше ніж annotate

            # ax.annotate(f"({x}, {y})", xy=(x, y), xytext=(5, 5),
            #             textcoords='offset points', fontsize=10)


    # Підписуємо осі
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_title('Coordinate Points Analysis', fontsize=14, fontweight='bold')
    ax.legend(loc='best') # Показує віконечко з усіма label=f"{point} ({quadrant}), обирає best місце

    # Автоматичне масштабування
    all_x = [p[0] for p in points if len(p) == 2]
    all_y = [p[1] for p in points if len(p) == 2]

    if all_x and all_y:
        # це для того, щоб "розширити" вікно графіка ще на 2 позиції від кожної крайньої точки з points
        # щоб точки не були притиснуті до краю, додати простору від них в сторону -x(-y) та +x(+y) на 2
        margin = 2
        ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
        ax.set_ylim(min(all_y) - margin, max(all_y) + margin)

    plt.tight_layout() # потрібен для автоматичного визначення, де розмістити і як краще припасувати label з легендою (віконечко з підписами точок)
    plt.show()


def get_points():
    """Receives point coordinates from the user"""
    points = []

    print("=" * 50)
    print("COORDINATE POINTS ANALYSIS")
    print("=" * 50)
    print("\nEnter the coordinates of the points.")
    print("To complete the entry, leave the field blank and press Enter.\n")

    point_count = 1
    while (True):
        print(f"\n--- Point {point_count} ---")

        x = input("Enter X coordinate: ").strip()
        if not x:
            break

        y = input("Enter Y coordinate: ").strip()
        if not y:
            break

        # в цьому випадку, якщо користувач натиснув Enter (хоче вийти) на X, то програма все одно запитує Y - це незручно
        # умова чекає вводу обох значень (X та Y), щоб подивитись, чи вони порожні
        # if not x or not y:
        #     break

        # те саме з цією умовою
        # if (x == "") or (y == ""):
        #     break

        try:
            # пробуємо конвертувати у float
            x_float = float(x)
            y_float = float(y)
            points.append([x_float, y_float])
            print(f"✓ Added point: ({x}, {y})")
            # якщо вдало конвертували та додали у список точок "points", то point_count += 1 (причина, чому це в блоці try)
            point_count += 1
        except ValueError:
            print("Error! Enter numbers (can be separated by a comma, for example: 3.5):")
            continue

    return points

# Testing
# test_points = [
#     [0, 0],      # Початок координат
#     [0, 5],      # Вісь Y
#     [4, 0],      # Вісь X
#     [3, 4],      # I чверть
#     [-2, 3],     # II чверть
#     [-3, -2],    # III чверть
#     [2, -3],     # IV чверть
#     [1, 4, -6]   # Некоректна точка
# ]
#
# # for p in test_points:
# #     analyze_coordinates(p)
# #     print()
# print("=== COORDINATE ANALYSIS ===\n")
# visualize_points(test_points)


def main():
    user_points = get_points()

    # Перевірка чи є точки
    if not user_points:
        print("\nNo points have been entered. Exiting.")
        return

    # Аналіз та візуалізація
    print("\n" + "=" * 50)
    print("ANALYSIS RESULTS")
    print("=" * 50 + "\n")

    visualize_points(user_points)


if __name__ == "__main__":
    main()
