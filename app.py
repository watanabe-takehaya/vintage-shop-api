from flask import Flask, jsonify, request

app = Flask(__name__)

shops_data = [
    {"name": "VINTAGE QOO TOKYO", "city": "東京", "address": "東京都渋谷区神宮前5-2-6", "description": "高級ブランド古着が充実"},
    {"name": "DEPT TOKYO", "city": "東京", "address": "東京都目黒区青葉台1-6-54", "description": "海外古着と家具が人気"},
    {"name": "BERBERJIN", "city": "東京", "address": "東京都渋谷区神宮前3-26-11", "description": "ヴィンテージデニムの名店"},
    {"name": "Chicago 原宿店", "city": "東京", "address": "東京都渋谷区神宮前6-31-21", "description": "着物と古着が豊富"},
    {"name": "AURA JAPON TOKYO", "city": "東京", "address": "東京都渋谷区神宮前3-28-5", "description": "欧州ブランド古着が人気"},
    {"name": "70B ANTIQUES 京都店", "city": "京都", "address": "京都府京都市中京区桝屋町53-1", "description": "英国アンティーク家具専門"},
    {"name": "mumokuteki antique&", "city": "京都", "address": "京都府京都市中京区式部町261", "description": "和洋レトロ雑貨が豊富"},
    {"name": "Antiques Truffle 京都店", "city": "京都", "address": "京都府京都市中京区堺町通錦小路上ル", "description": "欧州アンティーク食器が人気"},
    {"name": "70B ANTIQUES 大阪南堀江店", "city": "大阪", "address": "大阪府大阪市西区南堀江2-9-14", "description": "大型ヴィンテージ家具店"},
    {"name": "BEST VINTAGE 大阪", "city": "大阪", "address": "大阪府大阪市北区大深町4-20", "description": "高級ヴィンテージ時計専門"},
    {"name": "AURA 本店 梅田", "city": "大阪", "address": "大阪府大阪市北区中崎西2-4-20", "description": "海外ブランド古着が豊富"},
    {"name": "Pigsty アメ村店", "city": "大阪", "address": "大阪府大阪市中央区西心斎橋2-8-17", "description": "アメリカ古着が人気"},
    {"name": "CARA 福岡店", "city": "福岡", "address": "福岡県福岡市中央区天神2-11-1", "description": "一点物ブランド品が豊富"},
    {"name": "HUNT VINTAGE 福岡", "city": "福岡", "address": "福岡県福岡市中央区大名1-3-5", "description": "欧米ヴィンテージ古着専門"},
    {"name": "BEST VINTAGE 札幌", "city": "札幌", "address": "北海道札幌市中央区北3条西3-1", "description": "高級中古時計を多数販売"}
]

@app.route("/api/vintage-shops", methods=["GET"])
def get_shops():
    city_query = request.args.get('city')
    if city_query:
        filtered_shops = [shop for shop in shops_data if shop['city'] == city_query]
        return jsonify(filtered_shops)
    return jsonify(shops_data)

if __name__ == "__main__":
    app.run(debug=True)
