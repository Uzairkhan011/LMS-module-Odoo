{
    'name': "Library Management System",
    'summary': "This module will help you to manage your library",
    'description': """This Library Management System is designed to automate and streamline 
    the various processes involved in managing a library's resources and services. It provides 
    librarians and library staff with efficient tools to organize, catalog, track, and maintain
      a vast collection of books, periodicals, multimedia materials, and other resources.
         Additionally, it facilitates 
    patron management, circulation, and administrative tasks within the library.""",
    'author': "ERISP (Pvt) Ltd.",
    'website': "www.erisp.net",
    'category': 'Education',
    'depends': ['base'],
    'data': 
        [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'views/user_details.xml',
        'data/reference.xml'
        ],
    'application': True,
    'installable': True,
    'auto_install': False
}
