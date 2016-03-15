# -*- coding: utf-8 -*-
#  ©  2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from psycopg2._psycopg import IntegrityError
import openerp.tests.common as common


class TestPartnerIdentifierBase(common.TransactionCase):

    def test_base_functionalities(self):
        """Dummy CRUD test
        """
        partner_id_category = self.env['res.partner.id_category'].create({
            'code': 'id_code',
            'name': 'id_name',
        })
        self.assertEqual(partner_id_category.name, 'id_name')
        self.assertEqual(partner_id_category.code, 'id_code')

        partner_1 = self.env.ref('base.res_partner_1')
        self.assertEquals(len(partner_1.id_numbers), 0)
        with self.assertRaises(IntegrityError), self.cr.savepoint():
            partner_1.id_numbers = [(0, 0,  {
                'name': '1234',
            })]
        partner_1.id_numbers = [(0, 0,  {
            'name': '1234',
            'category_id': partner_id_category
        })]
        self.assertEquals(len(partner_1.id_numbers), 1)
        self.assertEquals(partner_1.id_numbers.name, '1234')
