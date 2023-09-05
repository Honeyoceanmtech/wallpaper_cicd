from flask_cors import CORS
from flask import Flask , request,jsonify
from pymongo import MongoClient

app=Flask(__name__)
CORS(app)

CONNECTION_STRING = "mongodb://admin:mnbhj34635koiuqweqwrq4547@142.93.212.228:27017/?authMechanism=DEFAULT"
# database = MongoClient(CONNECTION_STRING)['pexels_wallpaper']["pexels_wallpapers"]
# database = MongoClient(CONNECTION_STRING)['pexels_wallpaper']["wallpapers"]
database = MongoClient(CONNECTION_STRING)['pexels_wallpaper']["portrait_wallpapers"]
video_database = MongoClient(CONNECTION_STRING)['pexels_wallpaper']["live_wallpapers"]


Popular_AI_Background = [
    {'image_url':"https://images.pexels.com/photos/887821/pexels-photo-887821.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/772478/pexels-photo-772478.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/1292496/pexels-photo-1292496.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/4542275/pexels-photo-4542275.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/2157884/pexels-photo-2157884.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/3372831/pexels-photo-3372831.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/3719622/pexels-photo-3719622.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/5091507/pexels-photo-5091507.jpeg",'is_pro':'0'},
]

Tourism = [
    {'image_url':"https://images.pexels.com/photos/6858657/pexels-photo-6858657.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/2604792/pexels-photo-2604792.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/3087240/pexels-photo-3087240.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/4061694/pexels-photo-4061694.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/14292628/pexels-photo-14292628.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/13917011/pexels-photo-13917011.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/14193306/pexels-photo-14193306.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/15276645/pexels-photo-15276645/free-photo-of-parigi.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/6858673/pexels-photo-6858673.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/3255246/pexels-photo-3255246.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/754949/pexels-photo-754949.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/1480806/pexels-photo-1480806.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/6334003/pexels-photo-6334003.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/7770393/pexels-photo-7770393.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/891126/pexels-photo-891126.jpeg",'is_pro':'1'},
]

Nature = [
    {'image_url':"https://images.pexels.com/photos/1683492/pexels-photo-1683492.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/783795/pexels-photo-783795.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/1617365/pexels-photo-1617365.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/17081254/pexels-photo-17081254/free-photo-of-elephant-in-nature.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/220877/pexels-photo-220877.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/5846615/pexels-photo-5846615.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/15994923/pexels-photo-15994923/free-photo-of-trees-on-grass-in-park.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/10103015/pexels-photo-10103015.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/12552963/pexels-photo-12552963.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/5700270/pexels-photo-5700270.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/4864250/pexels-photo-4864250.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/716683/pexels-photo-716683.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/10560955/pexels-photo-10560955.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/10465332/pexels-photo-10465332.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/17388786/pexels-photo-17388786/free-photo-of-light-city-dawn-landscape.jpeg",'is_pro':'0'},
]

Wall_Backdrop = [
    {'image_url':"https://images.pexels.com/photos/1292496/pexels-photo-1292496.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/112811/pexels-photo-112811.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/129731/pexels-photo-129731.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/1234853/pexels-photo-1234853.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/1067556/pexels-photo-1067556.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/2168293/pexels-photo-2168293.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/7330788/pexels-photo-7330788.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/11285332/pexels-photo-11285332.png",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/9488899/pexels-photo-9488899.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/11236539/pexels-photo-11236539.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/9709852/pexels-photo-9709852.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/11453116/pexels-photo-11453116.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/14947258/pexels-photo-14947258.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/9471553/pexels-photo-9471553.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/4868968/pexels-photo-4868968.jpeg",'is_pro':'0'},
]

Birthday = [
    {'image_url':"https://images.pexels.com/photos/5404193/pexels-photo-5404193.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/15409846/pexels-photo-15409846/free-photo-of-creative-spring-background-with-carnations-and-gypsophila-flowers-and-copy-space.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/574282/pexels-photo-574282.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/4439461/pexels-photo-4439461.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/3825294/pexels-photo-3825294.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/3123915/pexels-photo-3123915.jpeg",'is_pro':'0'},
    {'image_url':"https://images.pexels.com/photos/2072181/pexels-photo-2072181.jpeg",'is_pro':'1'},
    {'image_url':"https://images.pexels.com/photos/7099953/pexels-photo-7099953.jpeg",'is_pro':'1'},
]


@app.route('/Background', methods=['GET'])
def Background():
    try:
        return jsonify([
                {'category_name':"Popular",'data':Popular_AI_Background},
                {'category_name':"Tourism",'data':Tourism},
                {'category_name':"Nature",'data':Nature},
                {'category_name':"Wall Backdrop",'data':Wall_Backdrop},
                {'category_name':"Birthday",'data':Birthday},
            ])
    except:
        return jsonify({'data':"Server Error"})

@app.route('/wallpaper_category', methods=['GET'])
def wallpaper_category():
    values = [
        {'category_name':"3D",'img_url':"https://images.pexels.com/photos/9977649/pexels-photo-9977649.jpeg",'live_img_url':"https://images.pexels.com/photos/10022926/pexels-photo-10022926.jpeg"},
        {'category_name':"Animal",'img_url':"https://images.pexels.com/photos/62324/leopard-safari-wildier-botswana-62324.jpeg",'live_img_url':"https://images.pexels.com/photos/7752793/pexels-photo-7752793.jpeg"},
        {'category_name':"Bright",'img_url':"https://images.pexels.com/photos/306864/pexels-photo-306864.jpeg",'live_img_url':"https://images.pexels.com/photos/954539/pexels-photo-954539.jpeg"},
        {'category_name':"Birds",'img_url':"https://images.pexels.com/photos/105808/pexels-photo-105808.jpeg",'live_img_url':"https://images.pexels.com/photos/2710186/pexels-photo-2710186.jpeg"},
        {'category_name':"Car",'img_url':"https://images.pexels.com/photos/4061977/pexels-photo-4061977.jpeg",'live_img_url':"https://images.pexels.com/photos/1592384/pexels-photo-1592384.jpeg"},
        {'category_name':"Church",'img_url':"https://images.pexels.com/photos/7168678/pexels-photo-7168678.jpeg",'live_img_url':"https://images.pexels.com/photos/6025586/pexels-photo-6025586.jpeg"},
        {'category_name':"City",'img_url':"https://images.pexels.com/photos/290275/pexels-photo-290275.jpeg",'live_img_url':"https://images.pexels.com/photos/234257/pexels-photo-234257.jpeg"},
        {'category_name':"Festival",'img_url':"https://images.pexels.com/photos/674723/pexels-photo-674723.jpeg",'live_img_url':"https://images.pexels.com/photos/4134548/pexels-photo-4134548.jpeg"},
        {'category_name':"Flower",'img_url':"https://images.pexels.com/photos/1075960/pexels-photo-1075960.jpeg",'live_img_url':"https://images.pexels.com/photos/1031965/pexels-photo-1031965.jpeg"},
        {'category_name':"Food Drink",'img_url':"https://images.pexels.com/photos/8738012/pexels-photo-8738012.jpeg",'live_img_url':"https://images.pexels.com/photos/2074108/pexels-photo-2074108.jpeg"},
        {'category_name':"Funny",'img_url':"https://images.pexels.com/photos/1214202/pexels-photo-1214202.jpeg",'live_img_url':"https://images.pexels.com/photos/994172/pexels-photo-994172.jpeg"},
        {'category_name':"Galaxy",'img_url':"https://images.pexels.com/photos/39561/solar-flare-sun-eruption-energy-39561.jpeg",'live_img_url':"https://images.pexels.com/photos/11272091/pexels-photo-11272091.jpeg"},
        {'category_name':"Game",'img_url':"https://images.pexels.com/photos/9099824/pexels-photo-9099824.jpeg",'live_img_url':"https://images.pexels.com/photos/792051/pexels-photo-792051.jpeg"},
        {'category_name':"Love",'img_url':"https://images.pexels.com/photos/2072185/pexels-photo-2072185.jpeg",'live_img_url':"https://images.pexels.com/photos/6798404/pexels-photo-6798404.jpeg"},
        {'category_name':"Nature",'img_url':"https://images.pexels.com/photos/1617365/pexels-photo-1617365.jpeg",'live_img_url':"https://images.pexels.com/photos/1683492/pexels-photo-1683492.jpeg"},
        {'category_name':"Night",'img_url':"https://images.pexels.com/photos/5864629/pexels-photo-5864629.jpeg",'live_img_url':"https://images.pexels.com/photos/706352/pexels-photo-706352.jpeg"},
        {'category_name':"Exclusive",'img_url':"https://wallpaperset.com/w/full/5/1/f/25965.jpg",'live_img_url':"https://images.pexels.com/photos/3098619/pexels-photo-3098619.jpeg"},
        {'category_name':"Popular",'img_url':"https://images.pexels.com/photos/17026789/pexels-photo-17026789/free-photo-of-false-barley.jpeg",'live_img_url':"https://images.pexels.com/photos/7968232/pexels-photo-7968232.jpeg"},
        {'category_name':"Quotes",'img_url':"https://images.pexels.com/photos/3309775/pexels-photo-3309775.jpeg",'live_img_url':"https://images.pexels.com/photos/4119140/pexels-photo-4119140.jpeg"},
    ]
    return jsonify(values)


@app.route('/live_wallpaper', methods=['POST'])
def live_wallpaper():
    image_urls = []
    category_name = request.form['category_name']
    page_no = request.form['page_no']
    
    result = video_database.aggregate([
        {
        '$match': {
            'category_name': category_name, 
            'page_no': int(page_no)
            }
        }
    ])

    for details in result:
        image_urls += (details['image_url'])
    try:
        if image_urls == []:
            return jsonify({'category_name':category_name,'image_urls':[]})
        else:
            return jsonify({'category_name':category_name,'image_urls':image_urls})
    except:
        return jsonify({'data':"Server Error"})


@app.route('/wallpaper', methods=['POST'])
def wallpaper():
    image_urls = []
    category_name = request.form['category_name']
    page_no = request.form['page_no']

    
    result = database.aggregate([
        {
        '$match': {
            'category_name': category_name, 
            'page_no': int(page_no)
            }
        }
    ])

    for details in result:
        image_urls += (details['image_url'])
    try:
        if image_urls == []:
            return jsonify({'category_name':category_name,'image_urls':[]})
        else:
            return jsonify({'category_name':category_name,'image_urls':image_urls})
    except:
        return jsonify({'data':"Server Error"})



if __name__=="__main__":
    app.run(port=83,host="0.0.0.0",debug=True)


