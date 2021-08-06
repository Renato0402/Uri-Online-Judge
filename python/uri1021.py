if __name__ == '__main__':
    # -*- coding: utf-8 -*-

    l1 = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    l2 = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    v = float(input())
    print("NOTAS:")
    for i in l1:
        x = v // i
        print(f"{x:.0f} nota(s) de R$ {i:.2f}")
        v = round(v - x * i, 2)

    print("MOEDAS:")
    for j in l2:
        y = round((v / j), 2)

        print(f"{int(str(y)[0])} moeda(s) de R$ {j:.2f}")
        v = round(v - int(str(y)[0]) * j, 2)