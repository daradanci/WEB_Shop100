from django.shortcuts import render

# Данные товаров (без БД)
clothes = [
    {"id": 1, "name": "Футболка Adidas", "price": 2500, "date": "2025-04-10", "description": "Качественная хлопковая футболка.", "image_url": "https://minio.example.com/1.jpg"},
    {"id": 2, "name": "Джинсы Levi's", "price": 1500, "date": "2025-04-12", "description": "Стильные джинсы из денима.", "image_url": "https://minio.example.com/2.jpg"},
    {"id": 3, "name": "Кроссовки Nike", "price": 3500, "date": "2025-04-15", "description": "Легкие и удобные кроссовки.", "image_url": "https://minio.example.com/3.jpg"},
]

# Данные корзины (без БД)
cart = {
    "id": 101,
    "clothes": [clothes[0], clothes[2]],  # В корзине товары 1 и 3
    "total_count": len([clothes[0], clothes[2]])
}

def clothes_list(request):
    """ Отображение списка товаров с фильтрацией """
    search_query = request.GET.get("search", "").strip().lower()
    filter_by = request.GET.get("filter_by", "all")
    
    filtered_clothes = clothes
    if search_query:
        filtered_clothes = [c for c in clothes if search_query in c["name"].lower() or search_query in str(c["price"]) or search_query in c["date"]]
    
    if filter_by == "price":
        filtered_clothes = sorted(filtered_clothes, key=lambda x: x["price"])
    elif filter_by == "date":
        filtered_clothes = sorted(filtered_clothes, key=lambda x: x["date"])
    
    return render(request, "clothes_list.html", {
        "clothes": filtered_clothes,
        "cart": cart,
        "search_query": search_query,
        "filter_by": filter_by
    })

def clothes_detail(request, clothes_id):
    """ Отображение подробной информации о товаре """
    item = next((c for c in clothes if c["id"] == clothes_id), None)
    return render(request, "clothes_detail.html", {"clothes": item})

def cart_detail(request):
    """ Отображение содержимого корзины """
    return render(request, "cart_detail.html", {"cart": cart})
