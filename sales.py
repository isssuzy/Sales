import math as m
import matplotlib.pyplot as plt



def read_sales_data(file_path):

    with open(f'{file_path}', 'r', encoding='utf-8') as file:

        sales = [];
        for line in file :

            data = line.strip().split(',')
            sale = {
                'product_name': data[0],
                'quantity': int(data[1]),
                'price': int(data[2]),
                'date': data[3]
            }
            sales.append(sale);

    return sales

def total_sales_per_product(sales_data) :
    total_sales = {}

    for sale in sales_data:

        if sale['product_name'] in total_sales:
            total_sales[sale['product_name']] += int(sale['quantity']) * int(sale['price'])
        else: total_sales[sale['product_name']] = int(sale['quantity']) * int(sale['price'])
    return total_sales

def sales_over_time(sales_data) :
    total_sales = {}

    for sale in sales_data:
        if sale['date'] in total_sales:
            total_sales[sale['date']] += int(sale['quantity']) * int(sale['price'])
        else:
            total_sales[sale['date']] = int(sale['quantity']) * int(sale['price'])
    return total_sales

def main() :
    
    file_path = 'sale_list'
    sales_data = read_sales_data(file_path);
    total_sales_per_product_data = total_sales_per_product(sales_data)
    sales_over_time_data = sales_over_time(sales_data)

    print('Продукт с максимальной прибылью:', max(total_sales_per_product_data, key=total_sales_per_product_data.get))
    print('День с максимальной прибылью:', max(sales_over_time_data, key=sales_over_time_data.get))

    plt.figure(1)
    plt.bar(total_sales_per_product_data.keys(), total_sales_per_product_data.values())
    plt.title('Общая сумма продаж по каждому продукту')
    plt.xlabel('Название продукта')
    plt.ylabel('Сумма продаж')

    plt.figure(2)
    plt.bar(sales_over_time_data.keys(), sales_over_time_data.values())
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж')

    plt.show()

if __name__ == '__main__':
    main()
