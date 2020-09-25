def migrate(cr, version):
    # update vsi_secret_code column 
    cr.execute('UPDATE account_invoice set vsi_secret_code = right(reference, 10), reference = name where length(reference) = 26 and vsi_status LIKE \'created\'')
