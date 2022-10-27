import pickle
import json
import numpy as np
import pandas as pd
import config

class SalesData() :
    def __init__(self, Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
       Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type, Item_Type , Outlet_Type) :

       self.Item_Weight = Item_Weight
       self.Item_Fat_Content = Item_Fat_Content
       self.Item_Visibility = Item_Visibility
       self.Item_MRP = Item_MRP
       self.Outlet_Identifier = Outlet_Identifier
       self.Outlet_Establishment_Year = Outlet_Establishment_Year
       self.Outlet_Size = Outlet_Size
       self.Outlet_Location_Type = Outlet_Location_Type
       self.Item_Type = "Item_Type_" + Item_Type
       self.Outlet_Type = "Outlet_Type_" + Outlet_Type

    def load_model (self) :
        with open (config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open (config.JSON_FILE_PATH) as f:
            self.json_data = json.load(f)

    def get_predicted_sales (self) :
        self.load_model()

        Item_Type_index = self.json_data["columns"].index(self.Item_Type)
        Outlet_Type_index = self.json_data["columns"].index(self.Outlet_Type)

        array = np.zeros(len(self.json_data["columns"]))

        array[0] = self.Item_Weight
        array[1] = self.json_data["Item_Fat_Content"][self.Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.Item_MRP
        array[4] = self.json_data["Outlet_Identifier"][self.Outlet_Identifier]
        array[5] = self.Outlet_Establishment_Year
        array[6] = self.json_data["Outlet_Size"][self.Outlet_Size]
        array[7] = self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        array[Item_Type_index] = 1
        array[Outlet_Type_index] = 1

        print ("Test Array :\n",array)
        predicted_sales = self.model.predict([array])[0]
        print ("Predicted Sales :",predicted_sales)
        return np.around(predicted_sales,2)

if __name__ == "__main__" :
    Item_Weight = 11.800
    Item_Fat_Content = "low fat"
    Item_Visibility = 0.081119
    Item_MRP = 190.3872
    Outlet_Identifier = "OUT019"
    Outlet_Establishment_Year = 2002
    Outlet_Size = "Small"
    Outlet_Location_Type = "Tier 1"
    Item_Type = "Dairy"
    Outlet_Type = "Supermarket Type3"

    sales_data = SalesData(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
       Outlet_Identifier, Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type, Item_Type , Outlet_Type)
    Sales = sales_data.get_predicted_sales()
    print ()
    print (f"Sales of Respective Outlet is {Sales}")