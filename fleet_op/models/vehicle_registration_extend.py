from odoo import fields, models


class VehicleRegistration(models.Model):

    _inherit = 'fleet.vehicle'


    is_vehicle = fields.Boolean(string="Vehicle")
    driver_identification_no = fields.Char(string="Driver Id")
    driver_contract_no = fields.Char(string="Driver contract no")
    vin_sn =fields.Char(sttring="Chassis number")
    income_aac_id = fields.Many2one('account.account',string="Income Account")
    expence_acc_id= fields.Many2one('account.account',string="Expence Account")
    First_contract_date =fields.Date(string="First Contract Date ")
    engine_no = fields.Char(string="Engine Number")
    co2 = fields.Float(string="Co2")
    # horsepower = fields.Integer(string="Horsepower")
    # horsepower_tax = fields.Float(string="Horsepower Taxaxtion")

    payment_deduction = fields.Float(string="Deduction")
    insurance_company_ids = fields.Many2one('res.partner', string="insurance company id")
    insurance_type_ids =fields.Many2one('res.partner', string="insurance type id")
    start_date_insurances = fields.Date(string="Start Insurance Date")
    end_insurance_dates = fields.Date(string="Start Insurance Date")
    policy_numbers = fields.Char(string="Policy Number")
    payments = fields.Float(string="Payment")
    payment_deductions = fields.Float(string="Deduction")
    vehicle_length = fields.Integer(string='Length(mm)')
    vehicle_width = fields.Integer(string='Width(mm)')
    vehicle_height = fields.Integer(string='Height(mm)')
    seat = fields.Integer(string="Seat")
    tire_size = fields.Char(string='Tire Size', size=64)
    tire_srno = fields.Char(string='Tire S/N', size=64)
    tire_issuance_date = fields.Date(string='Tire Issuance Date')
    battery_size = fields.Char(string='Battery Size', size=64)
    battery_srno = fields.Char(string='Battery S/N', size=64)
    battery_issuance_date = fields.Date(string='Battery Issuance Date')
    fuel_type = fields.Selection([('a','Disel'),('b','Petrol'),('c','CNG')])
    fuel_qty = fields.Float(string='Fuel quantity')
    fuel_capacity = fields.Float(string="Fuel Capacity")
    oil_name =fields.Char(string='Oil name')
    oil_capacity = fields.Float(string="Oil Capacity")
    history = fields.Html(string='History')

    last_service_date = fields.Date(string='Last Service From')
    last_service_date_to = fields.Date(string='Last Service To')
    next_service_date = fields.Date(string='Next Service From')
    next_service_date_to = fields.Date(string='Next Service To')
    last_service_by_id = fields.Many2one('res.partner',
                                         string="Last Service By")
    last_change_status_date = fields.Date(string='Last Status Changed Date',
                                          readonly=True)
    vehicle_location_id = fields.Many2one('res.country.state',string="Registration state")
    due_odometer = fields.Float(string='Next Service Odometer', readonly=True)
    due_odometer_unit = fields.Selection([('kilometers', 'Kilometers'),
                                          ('miles', 'Miles')],
                                            string = 'Due Odometer Units',
                                            help = 'Unit of the odometer ')
    acquisition_date =fields.Date(strin="Registration Date")
    model_no = fields.Char(string='Model No')
    warranty_period = fields.Char(string="warranty upto")
    update_by = fields.Many2one('res.user',string='Update By')
    update_date = fields.Date(string="update date")
    vechical_type_id = fields.Many2one('res.users',string="Vehicle Type")
    vechical_color_id = fields.Many2one('res.color',string="vehicle color")
    reg_id = fields.Many2one('res.users',string="Registerd By")
    vehicle_owner = fields.Many2one('res.partner',string="Vehicle owner")
    engine_no = fields.Char(string="Engine No")
    cylinder = fields.Char(string="No of cylender")
    engine_size = fields.Char(string="Engine Model")
    state = fields.Selection([('inspection', 'Draft'), ('in_progress','In Service'),
                              ('complete','Completed')], string="State")


class ResUsers(models.Model):
    """Res Users Model."""

    _inherit = "res.users"