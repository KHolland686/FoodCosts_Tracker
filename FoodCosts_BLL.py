from pint import UnitRegistry
from FoodCosts_DAL import FoodCosts_DAL

ureg = UnitRegistry()
#can input MySQLusername and password in following fields
dal = FoodCosts_DAL("localhost", "user", "password", "FoodCosts")

class FoodCosts_BLL:
    @staticmethod
    def convert_cost_to_target_unit(cost, current_unit, target_unit):
        cost_quantity = ureg.Quantity(cost, current_unit)
        base_unit_cost = cost_quantity.to(target_unit)
        return base_unit_cost.magnitude
    
    @staticmethod
    def calculate_average_costs(food_name, is_weighted = True):
        try:
            result = dal.fetch_total_cost_and_weight(food_name, is_weighted)

            total_cost, total_weight_or_count, unit_of_measure = result[0], result[1], result[2]

            if is_weighted and total_weight_or_count:
                avg_cost_per_unit = total_cost / total_weight_or_count
                avg_cost_per_ounce = FoodCosts_BLL.convert_cost_to_target_unit(avg_cost_per_unit, unit_of_measure, 'ounce')
                avg_cost_per_cup = FoodCosts_BLL.convert_cost_to_target_unit(avg_cost_per_unit, unit_of_measure, 'cup')
                avg_cost_per_pound = FoodCosts_BLL.convert_cost_to_target_unit(avg_cost_per_unit, unit_of_measure, 'pound')

                dal.update_average_costs(food_name, avg_cost_per_unit, avg_cost_per_ounce, avg_cost_per_cup, avg_cost_per_pound)
            elif not is_weighted and total_weight_or_count:
                avg_cost_per_unit = total_cost / total_weight_or_count
                dal.update_average_costs(food_name, avg_cost_per_unit, None, None, None) 
            else:
                print(f"No purchases found for {food_name}")

        except Exception as e:
            print(f"Error calculating and updating average costs for {food_name}: {str(e)}")

