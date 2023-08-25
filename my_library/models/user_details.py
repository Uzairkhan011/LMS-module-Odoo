
from flectra import models, fields, api
from datetime import datetime


class Author(models.Model):
    _description = 'Author'
    _name = 'author'

    name= fields.Char("Name") 

class Language(models.Model):
    _description = 'Language'
    _name = 'language'
    
    name= fields.Char("Name") 

class Countries(models.Model):
    _description = 'Countries'
    _name = 'countries'

    name= fields.Char("Name")

class Categories(models.Model):
    _description = 'Categories'
    _name = 'categories'

    name= fields.Char("Name") 

class BookDetail(models.Model):
    _description = 'book.detail'
    _name = 'book.detail'


    @api.model
    def _get_default_reference(self):
        # Get the current year
        current_year = datetime.now().year
        next_sequence = self.env["ir.sequence"].next_by_code(
            "book.detail.seq"
        )
        print(f"current_year: {current_year}, next_sequence: {next_sequence}")

        reference = f"BOOK{next_sequence}"

        return reference

    reference = fields.Char(
        string="Reference", readonly=True, copy=False, default=_get_default_reference
        )
    active = fields.Boolean(string="Active", default=True)


    def change_archive_state(self):
        if self.active:
            self.active=False
        else:
            self.active=True
    state =fields.Selection([('draft',"Draft"),('available','Available'),
                             ('lost','Lost')],default='draft',string ='Status')


    BOOK_TYPE = [
        ('compulsory', 'Compulsory'),
        ('general', 'General')
    ]

    name = fields.Char('Book', required=True)
    author = fields.Many2one("author", string="Author")
    date_release = fields.Date('Release Date', required=True)
    price = fields.Float('Price', required=True)
    categories = fields.Many2one("categories", string= "categories")
    book_type = fields.Selection(BOOK_TYPE, 'Book Type', equired=True)
    page_number = fields.Integer('Number of pages', required=True)
    Language = fields.Many2one("language", string="Language")
    priority = fields.Selection([
    ('1', ' '),
    ('2', 'Low'),
    ('3', 'Medium'),
    ('4', 'High')
    ], string='Reader rating', widget='selection')

    
    
    @api.constrains('name')
    def check_name(self):
        pass

    def action_avb(self):
        self.state = 'available'  


    def action_lost(self):
        self.state = 'lost'  


    def action_Rest(self):
        self.state = 'draft'  

class LibraryDetail(models.Model):
    _description = 'LibraryDetail'
    _name = 'library.detail'

    TYPE = [
        ('internal', 'Internal'),
        ('external', 'External')
    ]

    name = fields.Char('Name', required=True)
    house = fields.Char('House', required=True)
    street = fields.Char('Street', required=True)
    city = fields.Char('City', required=True)
    state_id = fields.Char('State', required=True)
    zip = fields.Integer('Zip', required=True)
    country_id= fields.Char('Country', required=True)
     
    address = fields.Char("Address")
    phone = fields.Integer('Phone', required=True)
    type = fields.Selection(TYPE, 'Type', required=True,store=True)
    book_id = fields.Many2many("book.detail", string="Book",)
    active = fields.Boolean(string="Active", default = True)

    def change_archive_state(self):
        if self.active:
            self.active=False
        else:
            self.active=True




  
    
    











