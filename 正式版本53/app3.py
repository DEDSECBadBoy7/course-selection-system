#    建立資料庫
import pymongo
import certifi
client = pymongo.MongoClient("mongodb+srv://youngman2023:youngman2023@cluster0.qovdh3t.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = client.test
collection =db.member_system#使用者(學生)
collection1 =db.staffmember_system#授權者(行政人員)
cllection2=db.lesson_system#存放課程
cllection3=db.lesson.ch_system#存放選課課程
print("資料夾建立成功")

#   建立flask伺服器
from flask import *
app = Flask(
    __name__,
    static_folder="public",
    static_url_path ="/"
)
app.secret_key = "any"

#     建立路由
@app.route("/")                                                 #----------學員登入頁面---------#
def indextest():
    return render_template("index.html")

@app.route("/studentsignup")                                    #---------學員註冊頁面---------#
def indextest2():
    return render_template("index.html2")

@app.route("/sus")                                              #---------成功提示頁面----------#
def indextest3():
    nickname= session["nickname"]
    email= session["email"]

    return render_template("sus.html",nickname=nickname,email=email)

@app.route("/member")                                           #---------學員首頁--------------#
def member():
    nickname= session["nickname"]
#權限控管
    if "nickname" in session:
        return render_template("member.html",nickname=nickname)
    else:
        return redirect("/")


@app.route("/lesson.ch")                                        #--------課程加選頁面-------#
def lessonch():


    nickname= session["nickname"]
    email= session["email"]
    #先取得符合email的資料
    collection =db.member_system
    result = collection.find_one({
    "email":email
    })
    #抓出科系和年級
    pointall=result["pointall"]
    grade=result["grade"]
    department=result["department"]
    abbreviation=result["abbreviation"]
    #用取得的科系年級重資料庫中找出課程資訊
    collection2 =db.lesson_system
    cur = collection2.find({
        "$and":[
            {"department":department},
            {"grade":grade}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)

    ])

#權限控管
    if "nickname" in session:
        return render_template("lesson.ch.html",pointall=pointall,cur=cur,abbreviation= abbreviation)
    else:
        return redirect("/")


@app.route("/lessonin1" ,methods = ["post"])                         #-------課程加選功能路由(1)-------*
def lessonin1():

    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode1 = int(request.form["newcode1"])
    session["newcode1"] = newcode1

    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode1":newcode1
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin2" ,methods = ["post"])                         #-------課程加選功能路由(2)-------*
def lessonin2():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode2 = int(request.form["newcode2"])
    session["newcode2"] = newcode2

    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode2":newcode2
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin3" ,methods = ["post"])                         #-------課程加選功能路由(3)-------*
def lessonin3():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode3 = int(request.form["newcode3"])
    session["newcode3"] = newcode3

    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode3":newcode3
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin4" ,methods = ["post"])                         #-------課程加選功能路由(4)-------*
def lessonin4():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode4 = int(request.form["newcode4"])
    session["newcode4"] = newcode4

    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode4":newcode4
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin5" ,methods = ["post"])                         #-------課程加選功能路由(5)-------*
def lessonin5():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode5 = int(request.form["newcode5"])
    session["newcode5"] = newcode5
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode5":newcode5
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin6" ,methods = ["post"])                         #-------課程加選功能路由(6)-------*
def lessonin6():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode6 = int(request.form["newcode6"])
    session["newcode6"] = newcode6
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode6":newcode6
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin7" ,methods = ["post"])                         #-------課程加選功能路由(7)-------*
def lessonin7():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode7 =int( request.form["newcode7"])
    session["newcode7"] = newcode7
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode7":newcode7
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin8" ,methods = ["post"])                         #-------課程加選功能路由(8)-------*
def lessonin8():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode8 =int( request.form["newcode8"])
    session["newcode8"] = newcode8
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode8":newcode8
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin9" ,methods = ["post"])                         #-------課程加選功能路由(9)-------*
def lessonin9():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode9 = int(request.form["newcode9"])
    session["newcode9"] = newcode9
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode9":newcode9
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin10" ,methods = ["post"])                         #-------課程加選功能路由(10)-------*
def lessonin10():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode10 =int( request.form["newcode10"])
    session["newcode10"] = newcode10
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode10":newcode10
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin11" ,methods = ["post"])                         #-------課程加選功能路由(11)-------*
def lessonin11():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode11 =int( request.form["newcode11"])
    session["newcode11"] = newcode11
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode11":newcode11
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin12" ,methods = ["post"])                         #-------課程加選功能路由(12)-------*
def lessonin12():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode12 =int( request.form["newcode12"])
    session["newcode12"] = newcode12
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode12":newcode12
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin13" ,methods = ["post"])                         #-------課程加選功能路由(13)-------*
def lessonin13():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode13 =int( request.form["newcode13"])
    session["newcode13"] = newcode13
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode13":newcode13
         }
     })
    return redirect("lesson.delete")
@app.route("/lessonin14" ,methods = ["post"])                         #-------課程加選功能路由(14)-------*
def lessonin14():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode14 =int( request.form["newcode14"])
    session["newcode14"] = newcode14
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode14":newcode14
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonin15" ,methods = ["post"])                         #-------課程加選功能路由(15)-------*
def lessonin15():
    #先取登入中人員的email
    email= session["email"]
    #從前端接收資料
    newcode15 =int( request.form["newcode15"])
    session["newcode15"] = newcode15
    #把資料放進資料庫,完成課程登入
    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "newcode15":newcode15
         }
     })
    return redirect("/lesson.delete")
@app.route("/lesson.delete")                                        #--------課程退選頁面-------#
def lessondelete():
    email= session["email"]
    #先取得符合email的資料
    collection =db.member_system
    result = collection.find_one({
    "email":email
    })
    #抓出選取的科目
    newcode1=result["newcode1"]
    newcode2=result["newcode2"]
    newcode3=result["newcode3"]
    newcode4=result["newcode4"]
    newcode5=result["newcode5"]
    newcode6=result["newcode6"]
    newcode7=result["newcode7"]
    newcode8=result["newcode8"]
    newcode9=result["newcode9"]
    newcode10=result["newcode10"]
    newcode11=result["newcode11"]
    newcode12=result["newcode12"]
    newcode13=result["newcode13"]
    newcode14=result["newcode14"]
    newcode15=result["newcode15"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode1
    })
    #抓出選取的科目資訊
    code1=result["code"]
    name1=result["name"]
    teacher1=result["teacher"]
    grade1=result["grade"]
    room1=result["room"]
    point1=int(result ["point"])
    start1=result["start"]
    end1=result["end"]
    day1=result["day"]
    field1=result["field"]
    information1=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode2
    })
    #抓出選取的科目資訊
    code2=result["code"]
    name2=result["name"]
    teacher2=result["teacher"]
    grade2=result["grade"]
    room2=result["room"]
    point2=int(result ["point"])
    start2=result["start"]
    end2=result["end"]
    day2=result["day"]
    field2=result["field"]
    information2=result["information"]
     #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode3
    })
    #抓出選取的科目資訊
    code3=result["code"]
    name3=result["name"]
    teacher3=result["teacher"]
    grade3=result["grade"]
    room3=result["room"]
    point3=int(result ["point"])
    start3=result["start"]
    end3=result["end"]
    day3=result["day"]
    field3=result["field"]
    information3=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode4
    })
    #抓出選取的科目資訊
    code4=result["code"]
    name4=result["name"]
    teacher4=result["teacher"]
    grade4=result["grade"]
    room4=result["room"]
    point4=int(result ["point"])
    start4=result["start"]
    end4=result["end"]
    day4=result["day"]
    field4=result["field"]
    information4=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode5
    })
    #抓出選取的科目資訊
    code5=result["code"]
    name5=result["name"]
    teacher5=result["teacher"]
    grade5=result["grade"]
    room5=result["room"]
    point5=int(result ["point"])
    start5=result["start"]
    end5=result["end"]
    day5=result["day"]
    field5=result["field"]
    information5=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode6
    })
    #抓出選取的科目資訊
    code6=result["code"]
    name6=result["name"]
    teacher6=result["teacher"]
    grade6=result["grade"]
    room6=result["room"]
    point6=int(result ["point"])
    start6=result["start"]
    end6=result["end"]
    day6=result["day"]
    field6=result["field"]
    information6=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode7
    })
    #抓出選取的科目資訊
    code7=result["code"]
    name7=result["name"]
    teacher7=result["teacher"]
    grade7=result["grade"]
    room7=result["room"]
    point7=int(result ["point"])
    start7=result["start"]
    end7=result["end"]
    day7=result["day"]
    field7=result["field"]
    information7=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode8
    })
    #抓出選取的科目資訊
    code8=result["code"]
    name8=result["name"]
    teacher8=result["teacher"]
    grade8=result["grade"]
    room8=result["room"]
    point8=int(result ["point"])
    start8=result["start"]
    end8=result["end"]
    day8=result["day"]
    field8=result["field"]
    information8=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode9
    })
    #抓出選取的科目資訊
    code9=result["code"]
    name9=result["name"]
    teacher9=result["teacher"]
    grade9=result["grade"]
    room9=result["room"]
    point9=int(result ["point"])
    start9=result["start"]
    end9=result["end"]
    day9=result["day"]
    field9=result["field"]
    information9=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode10
    })
    #抓出選取的科目資訊
    code10=result["code"]
    name10=result["name"]
    teacher10=result["teacher"]
    grade10=result["grade"]
    room10=result["room"]
    point10=int(result ["point"])
    start10=result["start"]
    end10=result["end"]
    day10=result["day"]
    field10=result["field"]
    information10=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode11
    })
    #抓出選取的科目資訊
    code11=result["code"]
    name11=result["name"]
    teacher11=result["teacher"]
    grade11=result["grade"]
    room11=result["room"]
    point11=int(result ["point"])
    start11=result["start"]
    end11=result["end"]
    day11=result["day"]
    field11=result["field"]
    information11=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode12
    })
    #抓出選取的科目資訊
    code12=result["code"]
    name12=result["name"]
    teacher12=result["teacher"]
    grade12=result["grade"]
    room12=result["room"]
    point12=int(result ["point"])
    start12=result["start"]
    end12=result["end"]
    day12=result["day"]
    field12=result["field"]
    information12=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode13
    })
    #抓出選取的科目資訊
    code13=result["code"]
    name13=result["name"]
    teacher13=result["teacher"]
    grade13=result["grade"]
    room13=result["room"]
    point13=int(result ["point"])
    start13=result["start"]
    end13=result["end"]
    day13=result["day"]
    field13=result["field"]
    information13=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode14
    })
    #抓出選取的科目資訊
    code14=result["code"]
    name14=result["name"]
    teacher14=result["teacher"]
    grade14=result["grade"]
    room14=result["room"]
    point14=int(result ["point"])
    start14=result["start"]
    end14=result["end"]
    day14=result["day"]
    field14=result["field"]
    information14=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode15
    })
    #抓出選取的科目資訊
    code15=result["code"]
    name15=result["name"]
    teacher15=result["teacher"]
    grade15=result["grade"]
    room15=result["room"]
    point15=int(result ["point"])
    start15=result["start"]
    end15=result["end"]
    day15=result["day"]
    field15=result["field"]
    information15=result["information"]
#權限控管
    pointall=int(point1+point2+point3+point4+point5+point6+point7+point8+point9+point10+point11+point12+point13+point14+point15)

    collection =db.member_system
    collection.update_one({
        "email":email
     },{
         "$set":{
             "pointall":pointall
         }
     })
    if "nickname" in session:
        return render_template("lesson.delete.html",field1=field1,field2=field2,field3=field3,field4=field4,field5=field5,field6=field6,field7=field7,field8=field8,field9=field9,field10=field10,field11=field11,field12=field12,field13=field13,field14=field14,field15=field15,pointall=pointall,day1=day1,day2=day2,day3=day3,day4=day4,day5=day5,day6=day6,day7=day7,day8=day8,day9=day9,day10=day10,day11=day11,day12=day12,day13=day13,day14=day14,day15=day15,start1=start1,end1=end1,start2=start2,end2=end2,start3=start3,end3=end3,start4=start4,end4=end4,start5=start5,end5=end5,start6=start6,end6=end6,start7=start7,end7=end7,start8=start8,end8=end8,start9=start9,end9=end9,start10=start10,end10=end10,start11=start11,end11=end11,start12=start12,end12=end12,start13=start13,end13=end13,start14=start14,end14=end14,start15=start15,end15=end15,code1=code1,grade1=grade1,point1=point1,room1=room1,teacher1=teacher1,name1=name1,information1=information1,code2=code2,grade2=grade2,point2=point2,room2=room2,teacher2=teacher2,name2=name2,information2=information2,code3=code3,grade3=grade3,point3=point3,room3=room3,teacher3=teacher3,name3=name3,information3=information3,code4=code4,grade4=grade4,point4=point4,room4=room4,teacher4=teacher4,name4=name4,information4=information4,code5=code5,grade5=grade5,point5=point5,room5=room5,teacher5=teacher5,name5=name5,information5=information5,code6=code6,grade6=grade6,point6=point6,room6=room6,teacher6=teacher6,name6=name6,information6=information6,code7=code7,grade7=grade7,point7=point7,room7=room7,teacher7=teacher7,name7=name7,information7=information7,code8=code8,grade8=grade8,point8=point8,room8=room8,teacher8=teacher8,name8=name8,information8=information8,code9=code9,grade9=grade9,point9=point9,room9=room9,teacher9=teacher9,name9=name9,information9=information9,code10=code10,grade10=grade10,point10=point10,room10=room10,teacher10=teacher10,name10=name10,information10=information10,code11=code11,grade11=grade11,point11=point11,room11=room11,teacher11=teacher11,name11=name11,information11=information11,code12=code12,grade12=grade12,point12=point12,room12=room12,teacher12=teacher12,name12=name12,information12=information12,code13=code13,grade13=grade13,point13=point13,room13=room13,teacher13=teacher13,name13=name13,information13=information13,code14=code14,grade14=grade14,point14=point14,room14=room14,teacher14=teacher14,name14=name14,information14=information14,code15=code15,grade15=grade15,point15=point15,room15=room15,teacher15=teacher15,name15=name15,information15=information15 )
    else:
        return redirect("/")


@app.route("/lessonout1" ,methods = ["post"])                         #-------課程退選功能路由(1)-------*
def lessonout():
    #從前端接收資料
    code1 = int(request.form["code1"])
    session["code1"] = code1
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode1":code1
     },{
         "$set":{
             "newcode1":"無資料"
         }
     })

    return redirect("/lesson.delete")
@app.route("/lessonout2" ,methods = ["post"])                         #-------課程退選功能路由(2)-------*
def lessonout2():
    #從前端接收資料
    code2 = int(request.form["code2"])
    session["code2"] = code2
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode2":code2
     },{
         "$set":{
             "newcode2":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout3" ,methods = ["post"])                         #-------課程退選功能路由(3)-------*
def lessonout3():
    #從前端接收資料
    code3 = int(request.form["code3"])
    session["code3"] = code3
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode3":code3
     },{
         "$set":{
             "newcode3":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout4" ,methods = ["post"])                         #-------課程退選功能路由(4)-------*
def lessonout4():
    #從前端接收資料
    code4 =int( request.form["code4"])
    session["code4"] = code4
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode4":code4
     },{
         "$set":{
             "newcode4":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout5" ,methods = ["post"])                         #-------課程退選功能路由(5)-------*
def lessonout5():
    #從前端接收資料
    code5 =int( request.form["code5"])
    session["code5"] = code5
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode5":code5
     },{
         "$set":{
             "newcode5":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout6" ,methods = ["post"])                         #-------課程退選功能路由(6)-------*
def lessonout6():
    #從前端接收資料
    code6 =int( request.form["code6"])
    session["code6"] = code6
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode6":code6
     },{
         "$set":{
             "newcode6":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout7" ,methods = ["post"])                         #-------課程退選功能路由(7)-------*
def lessonout7():
    #從前端接收資料
    code7 =int( request.form["code7"])
    session["code7"] = code7
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode7":code7
     },{
         "$set":{
             "newcode7":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout8" ,methods = ["post"])                         #-------課程退選功能路由(8)-------*
def lessonout8():
    #從前端接收資料
    code8 =int( request.form["code8"])
    session["code8"] = code8
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode8":code8
     },{
         "$set":{
             "newcode8":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout9" ,methods = ["post"])                         #-------課程退選功能路由(9)-------*
def lessonout9():
    #從前端接收資料
    code9 =int( request.form["code9"])
    session["code9"] = code9
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode9":code9
     },{
         "$set":{
             "newcode9":"無資料"
         }
     })
    return redirect("/lesson.delete")
@app.route("/lessonout10" ,methods = ["post"])                         #-------課程退選功能路由(10)-------*
def lessonout10():
    #從前端接收資料
    code10 =int( request.form["code10"])
    session["code10"] = code10
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode10":code10
     },{
         "$set":{
             "newcode10":"無資料"
         }
     })
    return redirect("/lesson.delete")

@app.route("/lessonout11" ,methods = ["post"])                         #-------課程退選功能路由(11)-------*
def lessonout11():
    #從前端接收資料
    code11 =int( request.form["code11"])
    session["code11"] = code11
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode11":code11
     },{
         "$set":{
             "newcode11":"無資料"
         }
     })
    return redirect("/lesson.delete")

@app.route("/lessonout12" ,methods = ["post"])                         #-------課程退選功能路由(12)-------*
def lessonout12():
    #從前端接收資料
    code12 =int( request.form["code12"])
    session["code12"] = code12
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode12":code12
     },{
         "$set":{
             "newcode12":"無資料"
         }
     })
    return redirect("/lesson.delete")

@app.route("/lessonout13" ,methods = ["post"])                         #-------課程退選功能路由(13)-------*
def lessonout13():
    #從前端接收資料
    code13 =int( request.form["code13"])
    session["code13"] = code13
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode13":code13
     },{
         "$set":{
             "newcode13":"無資料"
         }
     })
    return redirect("/lesson.delete")

@app.route("/lessonout14" ,methods = ["post"])                         #-------課程退選功能路由(14)-------*
def lessonout14():
    #從前端接收資料
    code14 =int( request.form["code14"])
    session["code14"] = code14
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode14":code14
     },{
         "$set":{
             "newcode14":"無資料"
         }
     })
    return redirect("/lesson.delete")

@app.route("/lessonout15" ,methods = ["post"])                         #-------課程退選功能路由(15)-------*
def lessonout15():
    #從前端接收資料
    code15 =int( request.form["code15"])
    session["code15"] = code15
    #把檢查資料庫,完成課程退選
    collection =db.member_system
    collection.update_one({
        "newcode15":code15
     },{
         "$set":{
             "newcode15":"無資料"
         }
     })
    return redirect("/lesson.delete")




@app.route("/lesson.if")                                         #----------課程資訊頁面----------#
def lessonif():
    nickname= session["nickname"]
#權限控管
    if "nickname" in session:
        return render_template("lesson.if.html",nickname=nickname)
    else:
        return redirect("/")


@app.route("/lesson.se")                                          #----------本學期課程頁面------------#
def lessonse():
    nickname= session["nickname"]
    email= session["email"]
    #先取得符合email的資料
    collection =db.member_system
    result = collection.find_one({
    "email":email
    })
    #抓出科系和年級
    grade=result["grade"]
    department=result["department"]
    #用取得的科系年級重資料庫中找出課程資訊
    collection2 =db.lesson_system
    cur = collection2.find({
        "$and":[
            {"department":department},
            {"grade":grade}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)

    ])
        #權限控管
    if "nickname" in session:
        return render_template("lesson.se.html",cur=cur,nickname=nickname)
    else:
        return


@app.route("/personal.if")                                          #------------個人資料頁面---------#
def personalif():

    nickname= session["nickname"]
    email= session["email"]
    collection =db.member_system
    result = collection.find_one({
    "email":email
    })
    pointall= result["pointall"]
    nickname=result["nickname"]
    grade=result["grade"]
    gender=result["gender"]
    department=result["department"]
    phone=result["phone"]
    address=result["address"]
    idnumber=result["idnumber"]
    year=result["year"]
    month=result["month"]
    day=result["day"]
#權限控管
    if "nickname" in session:
        return render_template("personal.if.html",pointall=pointall,nickname=nickname,grade=grade,department=department,gender=gender,idnumber=idnumber,phone=phone,address=address,year=year,month=month,day=day)
    else:
        return redirect("/")


@app.route("/personal.lesson")                                      #-------------個人課程清單-------------#
def personalle():
    email= session["email"]
    #先取得符合email的資料
    collection =db.member_system
    result = collection.find_one({
    "email":email
    })
    #抓出選取的科目
    pointall=result["pointall"]
    newcode1=result["newcode1"]
    newcode2=result["newcode2"]
    newcode3=result["newcode3"]
    newcode4=result["newcode4"]
    newcode5=result["newcode5"]
    newcode6=result["newcode6"]
    newcode7=result["newcode7"]
    newcode8=result["newcode8"]
    newcode9=result["newcode9"]
    newcode10=result["newcode10"]
    newcode11=result["newcode11"]
    newcode12=result["newcode12"]
    newcode13=result["newcode13"]
    newcode14=result["newcode14"]
    newcode15=result["newcode15"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode1
    })
    #抓出選取的科目資訊
    code1=result["code"]
    name1=result["name"]
    teacher1=result["teacher"]
    grade1=result["grade"]
    room1=result["room"]
    point1=int(result ["point"])
    start1=result["start"]
    end1=result["end"]
    day1=result["day"]
    field1=result["field"]
    information1=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode2
    })
    #抓出選取的科目資訊
    code2=result["code"]
    name2=result["name"]
    teacher2=result["teacher"]
    grade2=result["grade"]
    room2=result["room"]
    point2=int(result ["point"])
    start2=result["start"]
    end2=result["end"]
    day2=result["day"]
    field2=result["field"]
    information2=result["information"]
     #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode3
    })
    #抓出選取的科目資訊
    code3=result["code"]
    name3=result["name"]
    teacher3=result["teacher"]
    grade3=result["grade"]
    room3=result["room"]
    point3=int(result ["point"])
    start3=result["start"]
    end3=result["end"]
    day3=result["day"]
    field3=result["field"]
    information3=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode4
    })
    #抓出選取的科目資訊
    code4=result["code"]
    name4=result["name"]
    teacher4=result["teacher"]
    grade4=result["grade"]
    room4=result["room"]
    point4=int(result ["point"])
    start4=result["start"]
    end4=result["end"]
    day4=result["day"]
    field4=result["field"]
    information4=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode5
    })
    #抓出選取的科目資訊
    code5=result["code"]
    name5=result["name"]
    teacher5=result["teacher"]
    grade5=result["grade"]
    room5=result["room"]
    point5=int(result ["point"])
    start5=result["start"]
    end5=result["end"]
    day5=result["day"]
    field5=result["field"]
    information5=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode6
    })
    #抓出選取的科目資訊
    code6=result["code"]
    name6=result["name"]
    teacher6=result["teacher"]
    grade6=result["grade"]
    room6=result["room"]
    point6=int(result ["point"])
    start6=result["start"]
    end6=result["end"]
    day6=result["day"]
    field6=result["field"]
    information6=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode7
    })
    #抓出選取的科目資訊
    code7=result["code"]
    name7=result["name"]
    teacher7=result["teacher"]
    grade7=result["grade"]
    room7=result["room"]
    point7=int(result ["point"])
    start7=result["start"]
    end7=result["end"]
    day7=result["day"]
    field7=result["field"]
    information7=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode8
    })
    #抓出選取的科目資訊
    code8=result["code"]
    name8=result["name"]
    teacher8=result["teacher"]
    grade8=result["grade"]
    room8=result["room"]
    point8=int(result ["point"])
    start8=result["start"]
    end8=result["end"]
    day8=result["day"]
    field8=result["field"]
    information8=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode9
    })
    #抓出選取的科目資訊
    code9=result["code"]
    name9=result["name"]
    teacher9=result["teacher"]
    grade9=result["grade"]
    room9=result["room"]
    point9=int(result ["point"])
    start9=result["start"]
    end9=result["end"]
    day9=result["day"]
    field9=result["field"]
    information9=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode10
    })
    #抓出選取的科目資訊
    code10=result["code"]
    name10=result["name"]
    teacher10=result["teacher"]
    grade10=result["grade"]
    room10=result["room"]
    point10=int(result ["point"])
    start10=result["start"]
    end10=result["end"]
    day10=result["day"]
    field10=result["field"]
    information10=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode11
    })
    #抓出選取的科目資訊
    code11=result["code"]
    name11=result["name"]
    teacher11=result["teacher"]
    grade11=result["grade"]
    room11=result["room"]
    point11=int(result ["point"])
    start11=result["start"]
    end11=result["end"]
    day11=result["day"]
    field11=result["field"]
    information11=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode12
    })
    #抓出選取的科目資訊
    code12=result["code"]
    name12=result["name"]
    teacher12=result["teacher"]
    grade12=result["grade"]
    room12=result["room"]
    point12=int(result ["point"])
    start12=result["start"]
    end12=result["end"]
    day12=result["day"]
    field12=result["field"]
    information12=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode13
    })
    #抓出選取的科目資訊
    code13=result["code"]
    name13=result["name"]
    teacher13=result["teacher"]
    grade13=result["grade"]
    room13=result["room"]
    point13=int(result ["point"])
    start13=result["start"]
    end13=result["end"]
    day13=result["day"]
    field13=result["field"]
    information13=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode14
    })
    #抓出選取的科目資訊
    code14=result["code"]
    name14=result["name"]
    teacher14=result["teacher"]
    grade14=result["grade"]
    room14=result["room"]
    point14=int(result ["point"])
    start14=result["start"]
    end14=result["end"]
    day14=result["day"]
    field14=result["field"]
    information14=result["information"]
    #用取得的科目編碼從資料庫中找出課程資訊
    collection2 =db.lesson_system
    result = collection2.find_one({
    "code":newcode15
    })
    #抓出選取的科目資訊
    code15=result["code"]
    name15=result["name"]
    teacher15=result["teacher"]
    grade15=result["grade"]
    room15=result["room"]
    point15=int(result ["point"])
    start15=result["start"]
    end15=result["end"]
    day15=result["day"]
    field15=result["field"]
    information15=result["information"]
#權限控管

    if "nickname" in session:
        return render_template("personal.lesson.html",field1=field1,field2=field2,field3=field3,field4=field4,field5=field5,field6=field6,field7=field7,field8=field8,field9=field9,field10=field10,field11=field11,field12=field12,field13=field13,field14=field14,field15=field15,pointall=pointall,day1=day1,day2=day2,day3=day3,day4=day4,day5=day5,day6=day6,day7=day7,day8=day8,day9=day9,day10=day10,day11=day11,day12=day12,day13=day13,day14=day14,day15=day15,start1=start1,end1=end1,start2=start2,end2=end2,start3=start3,end3=end3,start4=start4,end4=end4,start5=start5,end5=end5,start6=start6,end6=end6,start7=start7,end7=end7,start8=start8,end8=end8,start9=start9,end9=end9,start10=start10,end10=end10,start11=start11,end11=end11,start12=start12,end12=end12,start13=start13,end13=end13,start14=start14,end14=end14,start15=start15,end15=end15,        code1=code1,grade1=grade1,point1=point1,room1=room1,teacher1=teacher1,name1=name1,information1=information1,code2=code2,grade2=grade2,point2=point2,room2=room2,teacher2=teacher2,name2=name2,information2=information2,code3=code3,grade3=grade3,point3=point3,room3=room3,teacher3=teacher3,name3=name3,information3=information3,code4=code4,grade4=grade4,point4=point4,room4=room4,teacher4=teacher4,name4=name4,information4=information4,code5=code5,grade5=grade5,point5=point5,room5=room5,teacher5=teacher5,name5=name5,information5=information5,code6=code6,grade6=grade6,point6=point6,room6=room6,teacher6=teacher6,name6=name6,information6=information6,code7=code7,grade7=grade7,point7=point7,room7=room7,teacher7=teacher7,name7=name7,information7=information7,code8=code8,grade8=grade8,point8=point8,room8=room8,teacher8=teacher8,name8=name8,information8=information8,code9=code9,grade9=grade9,point9=point9,room9=room9,teacher9=teacher9,name9=name9,information9=information9,code10=code10,grade10=grade10,point10=point10,room10=room10,teacher10=teacher10,name10=name10,information10=information10,code11=code11,grade11=grade11,point11=point11,room11=room11,teacher11=teacher11,name11=name11,information11=information11,code12=code12,grade12=grade12,point12=point12,room12=room12,teacher12=teacher12,name12=name12,information12=information12,code13=code13,grade13=grade13,point13=point13,room13=room13,teacher13=teacher13,name13=name13,information13=information13,code14=code14,grade14=grade14,point14=point14,room14=room14,teacher14=teacher14,name14=name14,information14=information14,code15=code15,grade15=grade15,point15=point15,room15=room15,teacher15=teacher15,name15=name15,information15=information15 )
    else:
        return redirect("/")


@app.route("/error")                                                 #-----------錯錯誤頁面--------#
def error():
    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("error.html",message = message)


@app.route("/signin",methods = ["post"])                              #--------登入功能路由-------#
def signin():
    #從前端取得使用者輸入
    email = request.form["email"]
    password =request.form["password"]
    # capthca=result["capthca"]

    #capthca =request.form["capthca"]
    #code =request.form["code"]
    #code =request.args.get["code"]
    #檢查信箱密碼是否正確
    collection =db.member_system
    result = collection.find_one({
       "$and":[
            {"email":email},
            {"password":password}

        ]
    })

    if result == None:
        return redirect("/error?msg=信箱或密碼輸入錯誤!")
    else:
        session["nickname"]=result["nickname"]
        session["email"] = result["email"]

        return redirect("/member")


@app.route("/signout")                                                  #---------登出功能路由-----------#
def signout():
#移除session中的會員資訊
    del session["nickname"]
    return redirect("/")


@app.route("/signup" ,methods = ["post"])                               #-----------註冊功能路由---------#
def signup():
    #從前端接收資料
    yearclass = request.form["yearclass"]
    nickname = request.form["nickname"]
    email = request.form["email"]
    password =request.form["password"]
    gender=request.form["gender"]
    department=request.form["department"]
    grade=int(request.form["grade" ])
    idnumber = request.form["idnumber"]
    address = request.form["address"]
    phone=request.form["phone"]
    year=request.form["year"]
    month=request.form["month"]
    day=request.form["day"]
    abbreviation=request.form["abbreviation"]
    session["nickname"] = nickname
    session["email"] = email
    #檢查是否有相同信箱
    result = collection.find_one({
        "email":email
        })
    if result != None:
        return redirect("/error?msg=信箱已經註冊過!")
    #把資料放進資料庫,完成註冊
    collection.insert_one({
        "yearclass":yearclass,
        "nickname" :nickname,
        "email" :email,
        "password":password,
        "gender":gender,
        "department":department,
        "grade":grade,
        "idnumber":idnumber,
        "address":address,
        "phone":phone,
        "year":year,
        "month":month,
        "day":day,
        "abbreviation":abbreviation,
        "pointall":0,
        "newcode1":"無資料",
        "newcode2":"無資料",
        "newcode3":"無資料",
        "newcode4":"無資料",
        "newcode5":"無資料",
        "newcode6":"無資料",
        "newcode7":"無資料",
        "newcode8":"無資料",
        "newcode9":"無資料",
        "newcode10":"無資料",
        "newcode11":"無資料",
        "newcode12":"無資料",
        "newcode13":"無資料",
        "newcode14":"無資料",
        "newcode15":"無資料"
     })
    return redirect("/sus")


@app.route("/test")#||||||測試||||||
def test():
    return render_template("test.html")
@app.route("/test2")#||||||測試||||||
def test2():
    return render_template("test2.html")

@app.route("/sample")
def sample():
    return render_template("sample.html")

@app.route("/sample2")
def gg():
    return render_template("sample2.html")

#/*******************************************************{行政人員區}****************************************************************************/


@app.route("/staff")                                     #||||||行政人員登入頁面||||||
def staff():
    return render_template("staffindex.html")

#-------------------------------------------------------------------[註冊授權人]----------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------#

@app.route("/staff2")                                     #||||||行政人員註冊登入頁面|||||
def staff2():
    return render_template("staffindex2.html")


@app.route("/staffsignin2",methods = ["post"])            #||||||行政人員註冊登入功能路由|||||
def staffsignin2():
    #從前端取得使用者輸入
    staffnumber = request.form["staffnumber"]
    password =request.form["password"]
    #檢查信箱密碼是否正確
    collection1 =db.staffmember_system
    result = collection1.find_one({
       "$and":[
            {"staffnumber":staffnumber},
            {"password":password}
        ]
    })
    if result == None:
        return redirect("/stafferror?msg=行政代碼或密碼輸入錯誤!")
    session[ "nickname" ]=result[ "nickname" ]
    return redirect("/newstaffsignup2")


@app.route("/newstaffsignup2")                            #||||||行政人員註冊首頁|||||
def newstaffsinup2():
    #權限控管
    if "nickname" in session:
        return render_template("newstaffsignup2.html")
    else:
        return redirect("/staff2")


@app.route("/staffsignup2" ,methods = ["post"])           #||||||行政人員註冊功能路由|||||
def staffsignup2():
    #從前端接收資料
    nickname = request.form["nickname"]
    session["nickname"] = nickname

    staffnumber = request.form["staffnumber"]
    session["staffnumber"] = staffnumber

    password =request.form["password"]
    session["password"] = password
    #檢查是否有相同行政代碼
    result = collection1.find_one({
        "staffnumber":staffnumber
        })
    if result != None:
        return redirect("/stafferror12?msg=行政代碼已經使用過!")

    #把資料放進資料庫,完成註冊
    collection1.insert_one({
        "nickname" :nickname,
        "staffnumber" :staffnumber,
        "password":password
     })
    return redirect("/staffsus2")


@app.route("/staffsignout2")                                                   #||||||行政人員註冊登出功能路由|||||
def staffsignout2():
#移除session中的會員資訊
    del session["nickname"]
    return redirect("/staff2")


@app.route("/stafferror12")                                                    #||||||行政人員註冊錯誤頁面||||||
def stafferror12():


    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("stafferror12.html",message = message)


@app.route("/staffsus2")                                                       #|||||行政人員註冊成功提示頁面|||||
def staffsus2():
    nickname= session["nickname"]
    staffnumber=session["staffnumber"]
    password=session["password"]
    return render_template("staffsus2.html",staffnumber=staffnumber,nickname=nickname,password=password)
#----------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------#


@app.route("/staffmember")                                                    #||||||行政人員首頁||||||
def staffmember():
    nickname= session["nickname"]
    #staffnumber= session["staffnumber"]
#權限控管
    if "nickname"in session:
        return render_template("staffmember.html",nickname=nickname)#nickname=nickname
    else:
        return redirect("/staff")


@app.route("/staffsignin",methods = ["post"])                                 #||||行政人員登入功能路由||||
def staffsignin():
    #從前端取得使用者輸入
    staffnumber = request.form["staffnumber"]
    password =request.form["password"]
    #檢查信箱密碼是否正確
    collection1 =db.staffmember_system
    result = collection1.find_one({
       "$and":[
            {"staffnumber":staffnumber},
            {"password":password}
        ]
    })
    if result == None:
        return redirect("/stafferror?msg=行政代碼或密碼輸入錯誤!")
    session[ "nickname" ]=result[ "nickname" ]
    return redirect("/staffmember")


@app.route("/staffsignout")                                                   #||||行政人員登出功能路由||||
def staffsignout():
#移除session中的會員資訊
    del session["nickname"]
    return redirect("/staff")


@app.route("/stafferror")                                                     #||||||行政頁面錯錯誤頁面||||||
def stafferror():
    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("stafferror.html",message = message)



#-------------------------------------------------------------[課程登入]------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------------------------#


@app.route("/arrangelesson")                                                 #||||||||||新增課程頁面||||||||||
def arrangelesson():
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangelesson.html")
    else:
        return redirect("/staff")



@app.route("/load" ,methods = ["post"])                                      #||||||課程加入功能路由||||||
def load():
    #從前端接收資料

   
    field = request.form["field"]
    session["field"] =field

    department = request.form["department"]
    session["department"] = department

    grade = int(request.form["grade"])
    session["grade"] = grade

    name = request.form["name"]
    session["name"] = name

    point = int(request.form["point"])
    session["point"] = point

    teacher = request.form["teacher"]
    session["teacher"] = teacher

    room = request.form["room"]
    session["room"] = room

    information = request.form["information"]
    session["information"] = information

    code = int(request.form["code"])
    session["code"] = code

    abbreviation = request.form["abbreviation"]
    session["abbreviation"] =abbreviation

    start = request.form["start"]
    session["start"] =start

    end = request.form["end"]
    session["end"] =end

    day = request.form["day"]
    session["day"] =day
    #檢查是否有相同課程
    collection2 =db.lesson_system
    result = collection2.find_one({
        "$and":[
            {"department":department},
            {"grade":grade},
            {"name":name}
        ]
    })
    if result != None:
        return redirect("/lessonarrangeerror?msg=課程已經登入!")

    #把資料放進資料庫,完成課程登入
    collection2 =db.lesson_system
    collection2.insert_one({
        "code":code,
        "department":department,
        "grade" :grade,
        "name":name,
        "point":point,
        "teacher":teacher,
        "room":room,
        "information":information,
        "abbreviation":abbreviation,
        "start":start,
        "end":end,
        "day":day,
        "field":field

     })
    return redirect("/lessonarrangesus")




@app.route("/lessonarrangesus")                                    #||||||課程登入成功提示頁面||||||
def lessonarrangesus():
    code=session["code"]
    department= session["department"]
    grade=session["grade"]
    name=session["name"]
    point= session["point"]
    room=session["room"]
    teacher=session["teacher"]
    information=session["information"]
    abbreviation=session["abbreviation"]
    start=session["start"]
    end=session["end"]
    day=session["day"]
    field=session["field"]
    return render_template("lessonarrangesus.html",field=field,abbreviation=abbreviation,code=code,department=department,grade=grade,point=point,room=room,teacher=teacher,name=name,information=information,start=start,end=end,day=day)





@app.route("/lessonarrangeerror")                                    #||||||課程登入錯誤頁面||||||
def lessonarrangeerror():
    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("lessonarrangeerror.html",message = message)



@app.route("/deletelesson")                                         #||||||||||註銷課程頁面||||||||||
def deltelesson():
 #權限控管
    if "nickname"in session:
        return render_template("staffdeletelesson.html")
    else:
        return redirect("/staff")

@app.route("/searchthelesson",methods = ["post"])                     #|||||搜尋課程功能路由||||||
def searchthelesson():
    #從前端接收資料
    department = request.form["department"]
    session["department"] =department
    grade =int(request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":department},
            {"grade":grade},
            {"code":code}
        ]
    })
    if result == None:
        return render_template("staffdeletelesson.html",name="查無資料",teacher="查無資料",grade="查無資料",room="查無資料",point="查無資料",code="查無資料")
    name=result["name"]
    teacher=result["teacher"]
    room=result["room"]
    point=result["point"]
    return render_template("staffdeletelesson.html",name=name,teacher=teacher,grade=grade,room=room,point=point,code=code)

@app.route("/deletethelesson",methods = ["post"])                     #|||||註銷課程功能路由||||||
def deletethelesson():
    #從前端接收資料
    department = request.form["department"]
    session["department"] =department
    grade =int(request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":department},
            {"grade":grade},
            {"code":code}
        ]
    })
    if result == None:
        return redirect("/deletelessonerror?msg=未找到相符課程!")
    #完成課程駐消除
    collection =db.lesson_system
    collection.delete_one({
        "$and":[
            {"department":department},
            {"grade":grade},
            {"code":code}
        ]
     })
    return redirect("/deletelessonsus")



@app.route("/deletelessonsus")                                    #||||||課程註消成功提示頁面||||||
def deletelessonsus():
    #code=session["code"]
    #department= session["department"]
    #grade=session["grade"]
    return render_template("staffdeletelessonsus.html")



@app.route("/deletelessonerror")                                    #||||||課程註冊錯誤頁面||||||
def deletelessonerrorr():
    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("staffdeletelessonerror.html",message = message)
#--------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------#


@app.route("/arrangestudentlaw")                                    #||||||管理學生頁面(法律系)||||||
def arrangestudentlaw():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"法律系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":4}
          ]
    })
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangestudentlaw.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")



@app.route("/searchaccountlaw",methods = ["post"])                     #|||||管理學生帳號功能路由(搜尋帳號----法律)||||||
def searchaccountlaw():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"法律系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"法律系"},
            {"grade":4}
          ]
    })

    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
       return render_template("staffarrangestudentlaw.html",nickname="查無資料",idnumber="查無資料",phone="查無資料",gender="查無資料",grade="查無資料",department="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    nickname=result["nickname"]
    gender=result["gender"]
    department=result["department"]
    grade=result["grade"]
    phone=result["phone"]
    idnumber=result["idnumber"]
    return render_template("staffarrangestudentlaw.html",nickname=nickname,idnumber=idnumber,phone=phone,gender=gender,grade=grade,department=department,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)


@app.route("/arrangestudentinformation")                              #||||||管理學生頁面(資管系)||||||
def arrangestudentinformation():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"資管系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":4}
          ]
    })
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangestudentinformation.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")


@app.route("/searchaccountinformation",methods = ["post"])                     #|||||管理學生帳號功能路由(搜尋帳號----資管)||||||
def searchaccountinformation():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"資管系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"資管系"},
            {"grade":4}
          ]
    })

    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
       return render_template("staffarrangestudentinformation.html",nickname="查無資料",idnumber="查無資料",phone="查無資料",gender="查無資料",grade="查無資料",department="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    nickname=result["nickname"]
    gender=result["gender"]
    department=result["department"]
    grade=result["grade"]
    phone=result["phone"]
    idnumber=result["idnumber"]
    return render_template("staffarrangestudentinformation.html",nickname=nickname,idnumber=idnumber,phone=phone,gender=gender,grade=grade,department=department,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)


@app.route("/arrangestudentmanage")                                          #||||||管理學生頁面(運籌系)||||||
def arrangestudentmanage():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"運籌系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":4}
          ]
    })
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangestudentmanage.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")


@app.route("/searchaccountmanage",methods = ["post"])                     #|||||管理學生帳號功能路由(搜尋帳號----資管)||||||
def searchaccountmanage():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"運籌系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":4}
          ]
    })

    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
       return render_template("staffarrangestudentmanage.html",nickname="查無資料",idnumber="查無資料",phone="查無資料",gender="查無資料",grade="查無資料",department="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    nickname=result["nickname"]
    gender=result["gender"]
    department=result["department"]
    grade=result["grade"]
    phone=result["phone"]
    idnumber=result["idnumber"]
    return render_template("staffarrangestudentmanage.html",nickname=nickname,idnumber=idnumber,phone=phone,gender=gender,grade=grade,department=department,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)



@app.route("/arrangestudenteconomic")                                          #||||||管理學生頁面(財管系)||||||
def arrangestudenteconomic():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"財管系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":4}
          ]
    })
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangestudenteconomic.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")


@app.route("/searchaccounteconomic",methods = ["post"])                     #|||||管理學生帳號功能路由(搜尋帳號----資管)||||||
def searchaccounteconomic():
    collection =db.member_system
    curin1 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":1}
        ]
    })
    collection =db.member_system
    curin2 = collection.find({
        "$and":[
            {"department":"財管系"},
           {"grade":2}
        ]
    })
    curin3 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":3}
        ]
    })
    curin4 = collection.find({
        "$and":[
            {"department":"財管系"},
            {"grade":4}
          ]
    })

    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
       return render_template("staffarrangestudenteconomic.html",nickname="查無資料",idnumber="查無資料",phone="查無資料",gender="查無資料",grade="查無資料",department="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    nickname=result["nickname"]
    gender=result["gender"]
    department=result["department"]
    grade=result["grade"]
    phone=result["phone"]
    idnumber=result["idnumber"]
    return render_template("staffarrangestudenteconomic.html",nickname=nickname,idnumber=idnumber,phone=phone,gender=gender,grade=grade,department=department,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)





@app.route("/arrangeaccount")                                          #||||||管理學生帳號頁面||||||
def arrangeaccount():
 #權限控管
    if "nickname"in session:
        return render_template("staffarrangeaccount.html")
    else:
        return redirect("/staff")


@app.route("/searchaccount",methods = ["post"])                     #|||||管理學生帳號功能路由(搜尋帳號)||||||
def searchaccount():
    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
       return render_template("staffarrangeaccount.html",nickname="查無資料",idnumber="查無資料",phone="查無資料",gender="查無資料",grade="查無資料",department="查無資料")
    nickname=result["nickname"]
    gender=result["gender"]
    department=result["department"]
    grade=result["grade"]
    phone=result["phone"]
    idnumber=result["idnumber"]
    return render_template("staffarrangeaccount.html",nickname=nickname,idnumber=idnumber,phone=phone,gender=gender,grade=grade,department=department)



@app.route("/deleteaccount",methods = ["post"])                     #|||||管理學生帳號功能路由(註銷帳號)||||||
def deleteaccount():
    #從前端接收資料
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber
    #檢查是否有相同課程
    collection=db.member_system
    result = collection.find_one({
       "idnumber": idnumber
    })
    if result == None:
        return redirect("/arrangeaccountrror?msg=未找到相符帳號!")
    #把資料放進資料庫,完成帳號駐消除
    collection =db.member_system
    collection.delete_one({
        "idnumber": idnumber
     })
    return redirect("/arrangeaccountsus")


@app.route("/arrangeaccountsus")                                    #||||||管理學生帳號頁面(註銷帳號)成功提示頁面||||||
def arrangeaccountsus():

    return render_template("satffarrangeaccountsus.html")


@app.route("/arrangeaccountrror")                                    #||||||管理學生帳號頁面(註銷帳號)錯誤頁面||||||
def arrangeaccountrror():
    message= request.args.get("msg"," ")#要求字串,/error?msg=錯誤訊息
    return render_template("staffarrangeaccountrror.html",message = message)







@app.route("/stafflessoninformation.se")                                #||||||查看課程頁面(資管)||||||
def stafflessoninformation():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":1}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":2}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin3 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":3}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])

    curin4 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":4}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
 #權限控管
    if "nickname"in session:
        return render_template("stafflessoninformation.se.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")


@app.route("/searchthelessoninformation",methods = ["post"])                     #|||||搜尋課程功能路由(資管)||||||
def searchthelessoninformation():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":1}
        ]
    })
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":2}
        ]
    })
    curin3 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":3}
        ]
    })
    curin4 = collection2.find({
        "$and":[
            {"department":"資管系"},
            {"grade":4}
        ]
    })
    #從前端接收資料
    grade = int(request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":"資管系"},
            {"grade":grade},
            {"code":code}
        ]
    })
    if result == None:
        return render_template("stafflessoninformation.se.html",name="查無資料",teacher="查無資料",grade="查無資料",room="查無資料",point="查無資料",code="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    name=result["name"]
    teacher=result["teacher"]
    room=result["room"]
    point=result["point"]
    return render_template("stafflessoninformation.se.html",name=name,teacher=teacher,grade=grade,room=room,point=point,code=code,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)


@app.route("/stafflessonlaw.se")                                         #||||||查看課程頁面(法律)||||||
def stafflessonlaw():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":1}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":2}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin3 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":3}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin4 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":4}
          ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
 #權限控管
    if "nickname"in session:
        return render_template("stafflessonlaw.se.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")



@app.route("/searchthelessonlaw",methods = ["post"])                     #|||||搜尋課程功能路由(法律)||||||
def searchthelessonlaw():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":1}
        ]
    })
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":2}
        ]
    })
    curin3 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":3}
        ]
    })
    curin4 = collection2.find({
        "$and":[
            {"department":"法律系"},
            {"grade":4}
        ]
    })
    #從前端接收資料
    grade =int( request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":"法律系"},
            {"grade":grade},
            {"code":code}
        ]
    })
    if result == None:
        return render_template("stafflessonlaw.se.html",name="查無資料",teacher="查無資料",grade="查無資料",room="查無資料",point="查無資料",code="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    name=result["name"]
    teacher=result["teacher"]
    room=result["room"]
    point=result["point"]
    return render_template("stafflessonlaw.se.html",name=name,teacher=teacher,grade=grade,room=room,point=point,code=code,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)


@app.route("/stafflessonmanage.se")                                         #||||||查看課程頁面(運籌)||||||
def stafflessonmanage():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":1}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"運籌系"},
           {"grade":2}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin3 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":3}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin4 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":4}
          ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
 #權限控管
    if "nickname"in session:
        return render_template("stafflessonmanage.se.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")



@app.route("/searchthelessonmanage",methods = ["post"])                     #|||||搜尋課程功能路由(法律)||||||
def searchthelessonmanage():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":1}
        ]
    })
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":2}
        ]
    })
    curin3 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":3}
        ]
    })
    curin4 = collection2.find({
        "$and":[
            {"department":"運籌系"},
            {"grade":4}
        ]
    })
    #從前端接收資料
    grade = int(request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":"運籌系"},
            {"grade":grade},
            {"code":code}
        ]
    })
    if result == None:
        return render_template("stafflessonmanage.se.html",name="查無資料",teacher="查無資料",grade="查無資料",room="查無資料",point="查無資料",code="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    name=result["name"]
    teacher=result["teacher"]
    room=result["room"]
    point=result["point"]
    return render_template("stafflessonmanage.se.html",name=name,teacher=teacher,grade=grade,room=room,point=point,code=code,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)



@app.route("/stafflessoneconomic.se")                                         #||||||查看課程頁面(財管)||||||
def stafflessoneconomic():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":1}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"財管系"},
           {"grade":2}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin3 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":3}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin4 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":4}
          ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
 #權限控管
    if "nickname"in session:
        return render_template("stafflessoneconomic.se.html",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    else:
        return redirect("/staff")



@app.route("/searchthelessoneconomic",methods = ["post"])                     #|||||搜尋課程功能路由(法律)||||||
def searchthelessoneconomic():
    collection2 =db.lesson_system
    curin1 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":1}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    collection2 =db.lesson_system
    curin2 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":2}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin3 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":3}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    curin4 = collection2.find({
        "$and":[
            {"department":"財管系"},
            {"grade":4}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    #從前端接收資料
    grade = int(request.form["grade"])
    session["grade"] =grade
    code = int(request.form["code"])
    session["code"] = code
    #檢查是否有相同課程
    collection=db.lesson_system
    result = collection.find_one({
       "$and":[
            {"department":"財管系"},
            {"grade":grade},
            {"code":code}
        ]
    },sort=[
        ("code",pymongo.ASCENDING)
                             ])
    if result == None:
        return render_template("stafflessoneconomic.se.html",name="查無資料",teacher="查無資料",grade="查無資料",room="查無資料",point="查無資料",code="查無資料",curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)
    name=result["name"]
    teacher=result["teacher"]
    room=result["room"]
    point=result["point"]
    return render_template("stafflessoneconomic.se.html",name=name,teacher=teacher,grade=grade,room=room,point=point,code=code,curin1=curin1,curin2=curin2,curin3=curin3,curin4=curin4)

#使用者修改密碼
@app.route("/changepassword1",methods = ["post"])
def changepassword1():
    #從前端接收資料
    password = request.form["password"]
    session["password"] =password
    email = request.form["email"]
    session["email"] =email
    newpassword = request.form["newpassword"]
    session["newpassword"] = newpassword
    newpassword1 = request.form["newpassword1"]
    session["newpassword1"] = newpassword1

    collection=db.member_system
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"password":password} ]
    })
    if result == None:
        return render_template("changepassworderror.html")
    newpassword = request.form["newpassword"]
    session["newpassword"] = newpassword
    # if newpassword == newpassword1=:
    #     return render_template()

    collection=db.member_system
    collection.update_one(
        {"email":email},
        {
         "$set":
             {"password":newpassword}

        })
    password= session["password"]
    return render_template("changepass.html",newpassword=newpassword)




@app.route("/changepassword")
def changepassword():
    return render_template("changepassword.html")

# @app.route("/mailerror")
# def mailerror():
#     return render_template("mailerror.html")

# @app.route("/mail2")
# def mail2():
#     return render_template("mail2.html")

#信箱寄送功能
@app.route("/resertpassword")
def resertpassword():
    return render_template("resertpassword.html")

@app.route("/mail",methods=["POST"])
def mail ():

    email = request.form["email"]
    session["email"] =email
    idnumber = request.form["idnumber"]
    session["idnumber"] =idnumber

    collection=db.member_system
    result = collection.find_one({
        "$and":[
            {"email":email},
            {"idnumber":idnumber} ]
    })

    if result == None:
        return render_template("mailerror.html")

    else:
        getemail=result["email"]
        import email.message
        msg=email.message.EmailMessage()
        msg["From"]="keway0108@gmail.com"
        msg["To"]=getemail
        msg["Subject"]="你好"

        getpasswprd=result["password"]
        getnickname=result["nickname"]
        msg.set_content("您好"+getnickname+","+"您的原始密碼為:"+getpasswprd)


        import smtplib

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("keway0108@gmail.com", "hdmujsjvihdlsfkw")
        server.send_message(msg)
        server.close()

        return render_template("mail2.html")

@app.route("/sendmail")
def sendmail():
    return render_template("sendmail.html")

@app.route("/sendmailerror")
def sendmail1():
    return render_template("sendmailerror.html")


@app.route("/sendmail2",methods=["POST"])
def sendmail2():

    email = request.form["email"]
    session["email"] =email

    collection=db.member_system
    result = collection.find_one({
    "email":email
    })

    if result == None:
        return render_template("sendmailerror.html")

    else:
        getemail=result["email"]
        import email.message
        msg=email.message.EmailMessage()
        msg["From"]="keway0108@gmail.com"
        msg["To"]=getemail
        msg["Subject"]="您好，可以開始選課了"

        getpasswprd=result["password"]
        getnickname=result["nickname"]
        msg.set_content("您好"+getnickname+","+"可以開始選課了:")


        import smtplib

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("keway0108@gmail.com", "hdmujsjvihdlsfkw")
        server.send_message(msg)
        server.close()

        return render_template("sendmails.html")


#  啟動伺服器
app.run(port =300)