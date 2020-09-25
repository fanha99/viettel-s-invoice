def migrate(cr, version):
    # Add fields
    cr.execute('ALTER TABLE account_invoice ADD vsi_pattern char, vsi_secret_code char')
