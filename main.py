from distutils.command.config import config
from flask import Flask,render_template,jsonify,request
from Model.utils import SalesData
import config

app = Flask(__name__)

@app.route("/")
def hello_flask() :
    print ("Welcome to Outlet Sales Prediction")
    return render_template ("index.html")

@app.route("/predict_Sales",methods = ["POST","GET"])
def Outlet_Sales () :

    if request.method == "GET" :
        print ("We are using GET Method")

        Item_Weight = float(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year = int(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Item_Type = request.args.get("Item_Type")
        Outlet_Type = request.args.get("Outlet_Type")

        print ("""Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type\n""",Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type)

        sales_data = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type)
        Sales = sales_data.get_predicted_sales()

        return render_template("index.html",prediction = Sales)

    else : 
        print ("We are using Post Method")

        Item_Weight = float(request.form.get("Item_Weight"))
        Item_Fat_Content = request.form.get("Item_Fat_Content")
        Item_Visibility = float(request.form.get("Item_Visibility"))
        Item_MRP = float(request.form.get("Item_MRP"))
        Outlet_Identifier = request.form.get("Outlet_Identifier")
        Outlet_Establishment_Year = int(request.form.get("Outlet_Establishment_Year"))
        Outlet_Size = request.form.get("Outlet_Size")
        Outlet_Location_Type = request.form.get("Outlet_Location_Type")
        Item_Type = request.form.get("Item_Type")
        Outlet_Type = request.form.get("Outlet_Type")

        print ("""Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type\n""",Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type)

        sales_data = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
        Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
        Outlet_Location_Type, Item_Type , Outlet_Type)
        Sales = sales_data.get_predicted_sales()

        return render_template("index.html",prediction = Sales)


if __name__ == "__main__" :
    app.run(host = "0.0.0.0",debug = True)