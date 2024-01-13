import mysql.connector

class FoodCosts_DAL:
    def __init__ (self, host, user, password, db):
        self.connection = mysql.connector.connect(host = host, user = user, password = password, database = db)
    
    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()

    def insert_food_item (self, food_name, department):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO FoodItems (FoodName, Department) VALUES (%s, %s)"
                cursor.execute(sql, (food_name, department))
            self.connection.commit()
            print (f"{food_name} successfully added!")
        except Exception as e:
            print(f"Error inserting {food_name}: {str(e)}")

    def record_purchase(self, food_name, weight, unit_cost, unit_of_measure):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO FoodPurchaseHistory (FoodName, Weight, CostPerUnit, UnitofMeasure) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (food_name, weight, unit_cost, unit_of_measure,))
                self.connection.commit()
                print(f"Purchase recorded for {food_name}")

        except Exception as e:
            print(f"Error recording purchase for {food_name}: {str(e)}")

    def update_average_costs(self, food_name, avg_cost_per_unit, avg_cost_per_ounce, avg_cost_per_cup, avg_cost_per_pound):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE AverageCosts SET AvgCostPerUnit = %s, AvgCostPerOunce = %s, AvgCostPerCup = %s, AvgCostPerPound = %s WHERE Food = %s"
                cursor.execute(sql, (avg_cost_per_unit, avg_cost_per_ounce, avg_cost_per_cup, avg_cost_per_pound, food_name))
                self.connection.commit()
                print(f"Average costs updated for {food_name}")
        except Exception as e:
            print(f"Error updating average costs for {food_name}: {str(e)}")

    def fetch_total_cost_and_weight(self, food_name, is_weighted=True):
        try:
            with self.connection.cursor() as cursor:
                if is_weighted:
                    sql = "SELECT SUM(CostPerUnit), SUM(Weight), UnitofMeasure FROM FoodPurchaseHistory WHERE FoodName = %s AND IsWeighted = TRUE"
                else:
                    sql = "SELECT SUM(CostPerUnit), COUNT(*), UnitofMeasure FROM FoodPurchaseHistory WHERE FoodName = %s AND IsWeighted = FALSE"    
                cursor.execute(sql, (food_name,))
                result = cursor.fetchone()

                return result

        except Exception as e:
            print(f"Error fetching total cost and weight for {food_name}: {str(e)}")
            return None
