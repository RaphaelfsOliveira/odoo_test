from odoo import models, fields


class NutriTable(models.Model):
    _name = 'nutri.model'

    name = fields.Char(string='Product')
    serv_size = fields.Char(string='Serving Size')
    cal = fields.Float(string='Calories')
    total_fat = fields.Float(string='Total Fat')
    satured_fat = fields.Float(string='Satured Fat')
    trans_fat = fields.Float(string='Trans Fat')
    poly_fat = fields.Float(string='Polyunsaturated Fat')
    mono_fat = fields.Float(string='Monounsaturated Fat')
    cholest = fields.Float(string='Cholesterol')
    sodium = fields.Float(string='Sodium')
    potassium = fields.Float(string='Potassium')
    total_carb = fields.Float(string='Total Carbohydrate')
    fiber = fields.Float(string='Dietary Fiber')
    sugar = fields.Float(string='Sugars')
    protein = fields.Float(string='Protein')
    vit_a = fields.Float(string='Vitamin A')
    vit_c = fields.Float(string='Vitamin C')
    calcium = fields.Float(string='Calcium')
    iron = fields.Float(string='Iron')
    phosp = fields.Float(string='Phosphorus')
    magne = fields.Float(string='Magnesium')
    zinc = fields.Float(string='Zinc')
    copper = fields.Float(string='Copper')
    un_pts = fields.Integer(string='Unofficial Pts')
    final_fat = fields.Float(string='Fat')
    final_carb = fields.Float(string='Carb')
    final_protein = fields.Float(string='Protein')
