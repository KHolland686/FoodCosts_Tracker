import FoodCosts_DAL
import FoodCosts_BLL

class FoodCosts_UI:
    @staticmethod
    def get_mysql_credentials():
        host = input("Enter MySQL host: ")
        user = input("Enter MySQL user: ")
        password = input("Enter MySQL password: ")
        db = input("Enter MySQL databse: ")
        return host, user, password, db
    
    @staticmethod
    def get_food_item_info():
        food_name = input("Enter name of food item: ")
        department = int(input("Enter department name: "))
        return food_name, department
    
    @staticmethod
    def get_purchase_info():
        food_name = input("Enter food name: ")
        weight = float(input("Enter weight: "))
        unit_cost = float(input("Enter cost per unit: "))
        current_unit = input("Enter unit of measurement (eg. ounces): ")
        return food_name, weight, unit_cost, current_unit
    
    @staticmethod
    def record_purchase():
        food_name, weight, unit_cost, current_unit = FoodCosts_UI.get_purchase_info()
        FoodCosts_BLL.record_purchase_with_unit_conversion(food_name, weight, unit_cost, current_unit)
