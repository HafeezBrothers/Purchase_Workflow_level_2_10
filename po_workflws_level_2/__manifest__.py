{

    'name':'Purchase Order WorkFlows (Level 2)',
    'description' : 'PO WorkFlows',
    'author' : 'Hafeez Brothers',
    'version': '1.0',
    
    'depends' : [
                   'base', 'purchase',
                ],
    'data' :[   
                
                'views/purchase_cus.xml',
                'security/hr_user_rights1.xml'
            ],
    'installable' : True,
    'price':40.00,
    'currency':'EUR', 
    

}
