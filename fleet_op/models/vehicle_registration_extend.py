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


class Respartner(models.Model):
    """Res Users Model."""

    _inherit = "res.partner"



class fleet_driver(models.Model):

    _inherit = 'res.partner'

    is_driver = fields.Boolean(string="is driver")



class odoometer(models.Model):
    _name = "odoometer"
    description= "odoometr detals"

    name = fields.Char(string="Name")
    vehicle_id = fields.Many2one("fleet.vehicle",string="vehicle id")
    number = fields.Float(string="odoometer increment")



class ColorColor(models.Model):
    """Model Color."""

    _name = 'color.color'
    _description = 'Colors'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')



class NextServiceDays(models.Model):
    """Model Next Service Days."""

    _name = 'next.service.days'
    _description = 'Next Service days'

    name = fields.Char(string='Name', translate=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle Id')
    days = fields.Integer(string='Days')



class RepairType(models.Model):
    """Repair Type."""

    _name = 'repair.type'
    _description = 'Vehicle Repair Type'

    name = fields.Char(string='Repair Type', size=264,
                       translate=True)

class NextIncrementNumber(models.Model):
    """Model Next Increment NUmber."""

    _name = 'next.increment.number'
    _description = 'Next Increment Number'

    name = fields.Char(string='Name', size=64, translate=True)
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle Id')
    number = fields.Float(string='Odometer Increment')


class DamageTypes(models.Model):
    """Model Damage Types."""

    _name = 'damage.types'
    _description = 'Damage Types'

    name = fields.Char(string='Name', traslate=True)
    code = fields.Char(string='Code')


class VehicleType(models.Model):
    """Model Vehicle Type."""

    _name = 'vehicle.type'
    _description = 'Vehicle Type'

    name = fields.Char(string="name")




class FleetVehicleAdvanceSearch(models.TransientModel):
    """Model fleet vehicle advance search."""

    _name = 'fleet.vehicle.advance.search'
    _description = 'Vehicle Advance Search'
    _rec_name = 'fmp_id'

    fmp_id = fields.Many2one('fleet.vehicle', string="Vehicle ID")
    vehicle_location_id = fields.Many2one('res.country.state',
                                          string='Province')
    state = fields.Selection([('inspection', 'Inspection'),
                              ('in_progress', 'In Progress'),
                              ('complete', 'Completed'),
                              ('released', 'Released'),
                              ('write-off', 'Write-Off')], string='Status')
    vehical_color_id = fields.Many2one('color.color', string='Color')
    vin_no = fields.Char(string='Vin No', size=64)
    engine_no = fields.Char(string='Engine No', size=64)
    last_service_date = fields.Date(string='Last Service From')
    last_service_date_to = fields.Date(string='Last Service To')
    next_service_date = fields.Date(string='Next Service From')
    next_service_date_to = fields.Date(string='Next Service To')
    acquisition_date = fields.Date(string="Registration From")
    acquisition_date_to = fields.Date(string="Registration To")
    release_date_from = fields.Date(string='Released From')
    release_date_to = fields.Date(string='Released To')
    driver_identification_no = fields.Char(string='Driver ID', size=64)
    vechical_type_id = fields.Many2one('vehicle.type', string='Vechical Type')
    division_id = fields.Many2one('vehicle.divison', string="Division")
    make_id = fields.Many2one("fleet.vehicle.model.brand", string="Make")
    model_id = fields.Many2one("fleet.vehicle.model", string="Model")



class FleetWorkOrderSearch(models.TransientModel):
    """Fleet Workorder search model."""

    _name = 'fleet.work.order.search'
    _description = 'Fleet Workorder Search'
    _rec_name = 'state'

    priority = fields.Selection([('normal', 'NORMAL'), ('high', 'HIGH'),
                                 ('low', 'LOW')], string='Order Priority')
    state = fields.Selection([('confirm', 'Open'), ('done', 'Close'),
                              ('any', 'Any')], string='Status')
    part_id = fields.Many2one('product.product', string='Parts')
    issue_date_from = fields.Date(string='Issue From')
    issue_date_to = fields.Date(string='Issue To')
    open_date_from = fields.Date(string='Open From')
    open_date_to = fields.Date(string='Open To')
    close_date_form = fields.Date(string='Close From')
    close_date_to = fields.Date(string='Close To')
    vehical_division_id = fields.Many2one('vehicle.divison',
                                          string="Division")
    work_order_id = fields.Many2one('fleet.vehicle.log.services',
                                    string='Service Order')
    fmp_id = fields.Many2one('fleet.vehicle', string='Vehicle ID')
    cost_subtype_id = fields.Many2one('fleet.service.type',
                                      string='Service Type')
    repair_type_id = fields.Many2one('repair.type', string='Repair Type')
    # open_days = fields.Char(string='Open Days', size=16)
    make_id = fields.Many2one("fleet.vehicle.model.brand", string="Make")
    model_id = fields.Many2one("fleet.vehicle.model", string="Model")


class FleetWittenOff(models.Model):
    """Model Fleet Witten Off."""

    _name = 'fleet.wittenoff'
    _description = 'Wittenoff Vehicles'
    _order = 'id desc'
    _rec_name = 'vehicle_id'

    name = fields.Char(string="Name")
    fleet_id = fields.Integer(string='Fleet ID',
                              help="Take this field for data migration")
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle',
                                 required=True)
    vehicle_fmp_id = fields.Char(string='Vehicle ID', size=64)
    vin_no = fields.Char(string='Vin No', size=64, translate=True)
    color_id = fields.Many2one('color.color', string='Color')
    vehicle_plate = fields.Char(string='Vechicle Plate No.', translate=True)
    report_date = fields.Date(string='Report Date')
    odometer = fields.Float(string='Odometer')
    cost_esitmation = fields.Float(string='Cost Estimation')
    note_for_cause_damage = fields.Text(string='Cuause of Damage',
                                        translate=True)
    note = fields.Text(string='Note', translate=True)
    cancel_note = fields.Text(string='Cancel Note', translate=True)
    multi_images = fields.Many2many('ir.attachment',
                                    'fleet_written_off_attachment_rel',
                                    'writeoff_id',
                                    'attachment_id', string='Multi Images')
    damage_type_ids = fields.Many2many('damage.types', 'fleet_wittenoff_damage_types_rel',
                                       'write_off_id', 'damage_id', string="Damage Type")
    repair_type_ids = fields.Many2many('repair.type', 'fleet_wittenoff_repair_types_rel',
                                       'write_off_id', 'repair_id', string="Repair Type")
    location_id = fields.Many2one('vehicle.location', string='Location')
    driver_id = fields.Many2one('res.partner', string='Driver')
    write_off_type = fields.Selection([
        ('general_accident', 'General Accident'),
        ('insurgent_attack', 'Insurgent Attack')],
        string='Write-off Type', default='general_accident')
    contact_no = fields.Char(string='Driver Contact Number')
    odometer_unit = fields.Selection([('kilometers', 'Kilometers'),
                                      ('miles', 'Miles')],
                                     string='Odometer Unit',
                                     help='Unit of the odometer ')
    province_id = fields.Many2one('res.country.state', 'Registration State')
    division_id = fields.Many2one('vehicle.divison', 'Division')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('cancel', 'Cancelled')],
                             string='State', default='draft')
    date_cancel = fields.Date(string='Date Cancelled')
    cancel_by_id = fields.Many2one('res.users', string="Cancelled By")


