from django.shortcuts import render

# Данные товаров (без БД)
clothes = [
    {"id": 1, "name": "Forest Coat", "price": 2500, "date": "2025-04-10", 
     "description": "Утепленное пальто в стиле природного минимализма.",
     "image_url": "http://127.0.0.1:3010/shop100-images/forest_coat.jpg"},
    {"id": 2, "name": "Goth Sweater", "price": 5500, "date": "2025-04-12", 
     "description": "Черный свитер с готическими узорами и удобной посадкой.",
     "image_url": "http://127.0.0.1:3010/shop100-images/goth_sweater.jpg"},
    {"id": 3, "name": "Night Velvet Boots", "price": 7500, "date": "2025-04-15", 
     "description": "Элегантные сапоги из ночного бархата для стильных образов.",
     "image_url": "http://127.0.0.1:3010/shop100-images/night_velvet_boots.jpg"},
    {"id": 4, "name": "Night Velvet Jacket", "price": 12500, "date": "2025-04-18", 
     "description": "Куртка из темного бархата с глубоким блеском.",
     "image_url": "http://127.0.0.1:3010/shop100-images/night_velvet_jacket.jpg"},
    {"id": 5, "name": "Fire Jeans", "price": 2200, "date": "2025-04-20", 
     "description": "Яркие джинсы с огненным оттенком и прочной тканью.",
     "image_url": "http://127.0.0.1:3010/shop100-images/fire_jeans.jpg"}
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
