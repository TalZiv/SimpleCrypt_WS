from simplecrypttools import CryptTools
from Crypto.PublicKey import RSA
import unittest
import base64


class SimpleCryptToolsTests(unittest.TestCase):

    def setUp(self):
        unittest.TestLoader.sortTestMethodsUsing = None
        self.cryptapi = CryptTools()
        self.passphrase = '$3©R3t©0d3'
        self.text = b'The quick brown fox jumps over the lazy dog'
        self.text_b64 = b'VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZw=='
        self.known_encrypted_text = base64.b64decode('LS1FSDBkBzl7JE43x9fxdhIk49Wd16lm6Ry26Culn6lGrECMScYDImOtB65lQyqya'
                                                     'IYkkfXRpDeH7TlIxSTgqbFq6ke0Wv/kgosFD9uF624WQLK6EoXGQjwaIAwFa3JsiK'
                                                     'eSVnxcgCHG8Ljy8P5a7fxROCStyi4Ese9yUTw77TY05ZTZ17fXlF8plV0dVvuwXoT'
                                                     'yuMKJAFY4VPYJk+1L66ORIl1l+ko8Nixh6MgKu9tO5TfXfCJDbRtvJZ/qgX9YHhzg'
                                                     'vkScd+oswCWMUWrsq3A7m2EGo0VlIIMvaqUU3enHtq2nMV4UGp7DcmCnxonk9R205'
                                                     'cTf3EsOH+gulF/dUABABsQCHu0JmCpU6rzB00op2rZhlxN7S3+v88G0fpdLP+ktbJ'
                                                     'Y0h4hlS11XaYJOk7daKb7F+PeLcRNpFAQ7A/0Jdo7ndhSSx4xgNA==')
        self.known_b64_encrypted_text = ('LS1FSDBkBzl7JE43x9fxdhIk49Wd16lm6Ry26Culn6lGrECMScYDImOtB65lQyqya'
                                         'IYkkfXRpDeH7TlIxSTgqbFq6ke0Wv/kgosFD9uF624WQLK6EoXGQjwaIAwFa3JsiK'
                                         'eSVnxcgCHG8Ljy8P5a7fxROCStyi4Ese9yUTw77TY05ZTZ17fXlF8plV0dVvuwXoT'
                                         'yuMKJAFY4VPYJk+1L66ORIl1l+ko8Nixh6MgKu9tO5TfXfCJDbRtvJZ/qgX9YHhzg'
                                         'vkScd+oswCWMUWrsq3A7m2EGo0VlIIMvaqUU3enHtq2nMV4UGp7DcmCnxonk9R205'
                                         'cTf3EsOH+gulF/dUABABsQCHu0JmCpU6rzB00op2rZhlxN7S3+v88G0fpdLP+ktbJ'
                                         'Y0h4hlS11XaYJOk7daKb7F+PeLcRNpFAQ7A/0Jdo7ndhSSx4xgNA==')
        self.predefined_private = base64.b64decode('LS0tLS1CRUdJTiBFTkNSWVBURUQgUFJJVkFURSBLRVktLS0tLQpNSUlGSlRCUEJna3F'
                                                   'oa2lHOXcwQkJRMHdRakFoQmdrckJnRUVBZHBIQkFzd0ZBUUkvZzJCQnllaWdFd0NBa0'
                                                   'FBCkFnRUlBZ0VCTUIwR0NXQ0dTQUZsQXdRQkFnUVE4T1l5YzM3UWxsR1d1blNRVFZ3V'
                                                   'FFBU0NCTkE2bmdpdy9XTGkKTlBaZENrc3QxZFZ1cE15MHc2ZFRTdm5neGs4SjJ4eisv'
                                                   'UEtoQ2RrVEhRUUFMSTg5dGw3WnhSbGwrZ1FUSW9NUQpoOFh4b1FFNTl2clFkYno1Ymk'
                                                   'yZ3BXM3NQdU1wcGI5Z1lYSkdrb1RZeGR2RUZ0YUt1SnI0VE9TcUZiek0xbmcwCmNlbD'
                                                   'E5cEloeUh5VzNGWGRhVERDZU1yNmd0OGJ2OXk5ODBXRkxQREJkUElQR1FhU0FzeWZYb'
                                                   'm9abzByM0J5MUYKMkl0YXVOdmtSckhMekZRTk5pcTdCK01jamZIRndIcUx4WWNsTGts'
                                                   'ajI3WXpjS3YxVzVYRlgzaHNxakVROU1VSwo5bld4NTlZY3JjZkZTSnltcUQ3d09hdEp'
                                                   'MREszTkp1MFVqQW1xK0F3ZkFwdWFCSzdMWXhUalMvL2J0S0MvbkJjClg2TEdCR3krVG'
                                                   'p4OE9JNjIvbmNTNzBiaEdwZmVSbSsyQXN0bjF5VUpYZE51a05oVk9CQmt2OXY3cjVUO'
                                                   'EYva3oKUVQxVGlhRjJDTDhlbnFZR0ZYL2pIZStlb3BMTVdONXpNMERWa0xlbDJkMVJn'
                                                   'NkU5dk1sc1J2WVh2RWh1VzNnWgpjc0wyUFNUWFBWZXVtZ0Z6RmFURkd4NE40THhrNzl'
                                                   'iTkphcENYdnVNOFc1RFNNMkJOaGtHdUZBR3RlMmQySldlCjFUSHA4amtJNlV5bzhNZ1'
                                                   'IxTTJRaUh1bjR1b0JBU3JZcGVSY0k4OVIvVE9POENDU2JzUEo5NjFnZ3ViejhiU04KT'
                                                   '3dsRGpNVEpuZEkzQno5QnpYaXA5Nmx4dHhldzRTS3NZVTkwZm45b2lHdjlvbS91QWJv'
                                                   'aVFTOWxHa1RQWkhaYQpOSWpBV3JhOVhYdHJIR3pUWldra2J1STgzVnI2WEQ4clZoZ09'
                                                   'sTjlpUXRIMzR3VVZ1UGswUE5UQVNwQk5jejRVCmdUa2ZFdEVnZ2lwVHBMckRKVEtESX'
                                                   'NxeUVBUHdxejNyR1lkZk1VRVRNb0FCVVI1Wk10bWIxZy9XNmJBWTRJcWcKRDlZN1VoS'
                                                   'GtYbzRPUzh6TlVTRTU1WHk4OStLMCtsczErUFliNnUzRXVZc2RQNUtwZEVkaGtUUnM3'
                                                   'LzZLcEtjRgpidFp2aHJXWDhoS0Q5a1VrNnhCZHVPMEJQVkJiZGV5THZEWks1dzdqZHd'
                                                   'rNy8zb3RvVzVCNDZOOWdCUnBpLzRMClRoL1F0YWw4RkJ1Z1JrUGpGNW1BUHFDc3JPNj'
                                                   'VUdVQzSTZHQWRqaFZMT3VTdWZMaXFmS3JOYm9jcXVkbFd0OVcKbjBrY3E4QXdZZzRmc'
                                                   'VJKL3JkTmpzSm5ZRXpQc3g4NG13RUpVa1RhYkJFbFRWS0tEd1JDc1FNajNpR1lhT2pq'
                                                   'NQpSKzcxOHZMVTFZVDFRVFZzRWxJdnZvNnVFL0Z2eVRVbjg0TWMzOG9QU0xMUm41YzZ'
                                                   '3VHZZb0VwZzBZeFJMbHU3CmV5bkx0OEM2eGEyM2hxaCtJaWN2V0xLajgyR2cxdDFmbl'
                                                   'dPMWVSVEtIVUwzWjA4NHhFZE42bzlaTnJFN1J1V1UKOGNxdUg2SG9FMXZNdFJVODMrb'
                                                   '0hpVXlNaFNpdURJZ29NbUdwNGpuaVE4VFpDa0Fack5BakVLckVzOE1aRndwRwpuNUVW'
                                                   'S1lqeW5zdEpJUHRySzhYUmpSZUxweWwwZ2d6SEEwQ3F1bHdqbWpYSURsUlNEMStOSUF'
                                                   'VVERIZXQvcFpWClFIbnVMcUVhUjNnazU2dWFvYkNOLzcwQnlHVHBIZnozWEwveHFOK2'
                                                   'VzOVdUYmhab1dkd3lVVzAvMGtxdUI5VEUKc1Bydk4xSW5UU2ZlS3AzTzRCeFo0Z0Jld'
                                                   '2ZpamFDK0ZYenFSZHpsQlJoY0psSVgvVkg1VDFiblUranU4ZmNHQgpiZUhGU1lsdkNh'
                                                   'SGZ0OVdNeDBNVzZUYzMwVW5RekNUVk1tM1c0UGMzWDVxaVVDMVcrQmswWituaHZWR3J'
                                                   'PYVFZCnFtYUFyd1JEem5MT0ZIZTEydGZ2MnAwYmp1ZDBNWjRoVHJQcVpZZ3lneDFqY0'
                                                   'lOc0JUMTBwUWJhSHZqcVAwTGsKSm53ZzVXQm9DYlc0cnRBT3hjNFFuNzZqNGkzQ20zS'
                                                   'lBLZ3B2Nkx6RmdrSGxPd2t0NUJ6VWJ3ZzBoM1piTm04RwpHWHhEK09HeEhPM0xoTlls'
                                                   'V0E3cHBjWE1HYlo5RDZUZ0xBPT0KLS0tLS1FTkQgRU5DUllQVEVEIFBSSVZBVEUgS0V'
                                                   'ZLS0tLS0=')
        self.b64_predefined_private = ('LS0tLS1CRUdJTiBFTkNSWVBURUQgUFJJVkFURSBLRVktLS0tLQpNSUlGSlRCUEJna3F'
                                       'oa2lHOXcwQkJRMHdRakFoQmdrckJnRUVBZHBIQkFzd0ZBUUkvZzJCQnllaWdFd0NBa0'
                                       'FBCkFnRUlBZ0VCTUIwR0NXQ0dTQUZsQXdRQkFnUVE4T1l5YzM3UWxsR1d1blNRVFZ3V'
                                       'FFBU0NCTkE2bmdpdy9XTGkKTlBaZENrc3QxZFZ1cE15MHc2ZFRTdm5neGs4SjJ4eisv'
                                       'UEtoQ2RrVEhRUUFMSTg5dGw3WnhSbGwrZ1FUSW9NUQpoOFh4b1FFNTl2clFkYno1Ymk'
                                       'yZ3BXM3NQdU1wcGI5Z1lYSkdrb1RZeGR2RUZ0YUt1SnI0VE9TcUZiek0xbmcwCmNlbD'
                                       'E5cEloeUh5VzNGWGRhVERDZU1yNmd0OGJ2OXk5ODBXRkxQREJkUElQR1FhU0FzeWZYb'
                                       'm9abzByM0J5MUYKMkl0YXVOdmtSckhMekZRTk5pcTdCK01jamZIRndIcUx4WWNsTGts'
                                       'ajI3WXpjS3YxVzVYRlgzaHNxakVROU1VSwo5bld4NTlZY3JjZkZTSnltcUQ3d09hdEp'
                                       'MREszTkp1MFVqQW1xK0F3ZkFwdWFCSzdMWXhUalMvL2J0S0MvbkJjClg2TEdCR3krVG'
                                       'p4OE9JNjIvbmNTNzBiaEdwZmVSbSsyQXN0bjF5VUpYZE51a05oVk9CQmt2OXY3cjVUO'
                                       'EYva3oKUVQxVGlhRjJDTDhlbnFZR0ZYL2pIZStlb3BMTVdONXpNMERWa0xlbDJkMVJn'
                                       'NkU5dk1sc1J2WVh2RWh1VzNnWgpjc0wyUFNUWFBWZXVtZ0Z6RmFURkd4NE40THhrNzl'
                                       'iTkphcENYdnVNOFc1RFNNMkJOaGtHdUZBR3RlMmQySldlCjFUSHA4amtJNlV5bzhNZ1'
                                       'IxTTJRaUh1bjR1b0JBU3JZcGVSY0k4OVIvVE9POENDU2JzUEo5NjFnZ3ViejhiU04KT'
                                       '3dsRGpNVEpuZEkzQno5QnpYaXA5Nmx4dHhldzRTS3NZVTkwZm45b2lHdjlvbS91QWJv'
                                       'aVFTOWxHa1RQWkhaYQpOSWpBV3JhOVhYdHJIR3pUWldra2J1STgzVnI2WEQ4clZoZ09'
                                       'sTjlpUXRIMzR3VVZ1UGswUE5UQVNwQk5jejRVCmdUa2ZFdEVnZ2lwVHBMckRKVEtESX'
                                       'NxeUVBUHdxejNyR1lkZk1VRVRNb0FCVVI1Wk10bWIxZy9XNmJBWTRJcWcKRDlZN1VoS'
                                       'GtYbzRPUzh6TlVTRTU1WHk4OStLMCtsczErUFliNnUzRXVZc2RQNUtwZEVkaGtUUnM3'
                                       'LzZLcEtjRgpidFp2aHJXWDhoS0Q5a1VrNnhCZHVPMEJQVkJiZGV5THZEWks1dzdqZHd'
                                       'rNy8zb3RvVzVCNDZOOWdCUnBpLzRMClRoL1F0YWw4RkJ1Z1JrUGpGNW1BUHFDc3JPNj'
                                       'VUdVQzSTZHQWRqaFZMT3VTdWZMaXFmS3JOYm9jcXVkbFd0OVcKbjBrY3E4QXdZZzRmc'
                                       'VJKL3JkTmpzSm5ZRXpQc3g4NG13RUpVa1RhYkJFbFRWS0tEd1JDc1FNajNpR1lhT2pq'
                                       'NQpSKzcxOHZMVTFZVDFRVFZzRWxJdnZvNnVFL0Z2eVRVbjg0TWMzOG9QU0xMUm41YzZ'
                                       '3VHZZb0VwZzBZeFJMbHU3CmV5bkx0OEM2eGEyM2hxaCtJaWN2V0xLajgyR2cxdDFmbl'
                                       'dPMWVSVEtIVUwzWjA4NHhFZE42bzlaTnJFN1J1V1UKOGNxdUg2SG9FMXZNdFJVODMrb'
                                       '0hpVXlNaFNpdURJZ29NbUdwNGpuaVE4VFpDa0Fack5BakVLckVzOE1aRndwRwpuNUVW'
                                       'S1lqeW5zdEpJUHRySzhYUmpSZUxweWwwZ2d6SEEwQ3F1bHdqbWpYSURsUlNEMStOSUF'
                                       'VVERIZXQvcFpWClFIbnVMcUVhUjNnazU2dWFvYkNOLzcwQnlHVHBIZnozWEwveHFOK2'
                                       'VzOVdUYmhab1dkd3lVVzAvMGtxdUI5VEUKc1Bydk4xSW5UU2ZlS3AzTzRCeFo0Z0Jld'
                                       '2ZpamFDK0ZYenFSZHpsQlJoY0psSVgvVkg1VDFiblUranU4ZmNHQgpiZUhGU1lsdkNh'
                                       'SGZ0OVdNeDBNVzZUYzMwVW5RekNUVk1tM1c0UGMzWDVxaVVDMVcrQmswWituaHZWR3J'
                                       'PYVFZCnFtYUFyd1JEem5MT0ZIZTEydGZ2MnAwYmp1ZDBNWjRoVHJQcVpZZ3lneDFqY0'
                                       'lOc0JUMTBwUWJhSHZqcVAwTGsKSm53ZzVXQm9DYlc0cnRBT3hjNFFuNzZqNGkzQ20zS'
                                       'lBLZ3B2Nkx6RmdrSGxPd2t0NUJ6VWJ3ZzBoM1piTm04RwpHWHhEK09HeEhPM0xoTlls'
                                       'V0E3cHBjWE1HYlo5RDZUZ0xBPT0KLS0tLS1FTkQgRU5DUllQVEVEIFBSSVZBVEUgS0V'
                                       'ZLS0tLS0=')
        self.predefined_public = base64.b64decode('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVG'
                                                  'QUFPQ0FROEFNSUlCQ2dLQ0FRRUF1RWk3SXNhcElnZnVxdEdtV3hNeQp1aFA5ZVVZci9G'
                                                  'TXV1UFZBQ2c3V3dUam11N3NlenVzOE1teFRLQmtrVUdZcURTQjg2My9vNExOL0RFbk1j'
                                                  'Q2t5Ci9oRWhVeXV1b0NDdDM1ekloOUJvc0c4bjFTYThJdTFwTy9WaWY4b2pacUhoVWFl'
                                                  'SGx0V3pNZDhnT2UrSmd3Y2IKQURrc0JBaGo5TmNNR1RNMThtc1d3UENXQ3FEbTdGSzh1'
                                                  'b1Y2RnVOZ1Z3Q2phcmFONmVvdjRWeEhJbFZOK0hIMQp3QU0vTmMvSlo2QUxwbmU4aTNr'
                                                  'cC8weWJJWG43MlJrYlB1QVlVaWNmc0R5a1BOT1hXSmR1S3c1VnhlK3MzdkgwCjJ5NXly'
                                                  'YXc4R2RMdHVnU1gvQ1E0bjlzN3V6NXVZZ3hLb1lXcm9uZjNpak9TSlE2YkVPQndmQ0Vx'
                                                  'V2t5SVRtVkoKTXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')
        self.b64_predefined_public = ('LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVG'
                                      'QUFPQ0FROEFNSUlCQ2dLQ0FRRUF1RWk3SXNhcElnZnVxdEdtV3hNeQp1aFA5ZVVZci9G'
                                      'TXV1UFZBQ2c3V3dUam11N3NlenVzOE1teFRLQmtrVUdZcURTQjg2My9vNExOL0RFbk1j'
                                      'Q2t5Ci9oRWhVeXV1b0NDdDM1ekloOUJvc0c4bjFTYThJdTFwTy9WaWY4b2pacUhoVWFl'
                                      'SGx0V3pNZDhnT2UrSmd3Y2IKQURrc0JBaGo5TmNNR1RNMThtc1d3UENXQ3FEbTdGSzh1'
                                      'b1Y2RnVOZ1Z3Q2phcmFONmVvdjRWeEhJbFZOK0hIMQp3QU0vTmMvSlo2QUxwbmU4aTNr'
                                      'cC8weWJJWG43MlJrYlB1QVlVaWNmc0R5a1BOT1hXSmR1S3c1VnhlK3MzdkgwCjJ5NXly'
                                      'YXc4R2RMdHVnU1gvQ1E0bjlzN3V6NXVZZ3hLb1lXcm9uZjNpak9TSlE2YkVPQndmQ0Vx'
                                      'V2t5SVRtVkoKTXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t')

    def test_key_pair_length(self):
        keys = self.cryptapi.generatekeypair(self.passphrase, key_size=2048)
        self.assertEqual(len(keys['private']), 1865)
        self.assertEqual(len(keys['public']), 450)

    def test_encryption(self):
        publickey = RSA.import_key(self.predefined_public)
        encrypted = self.cryptapi.encrypt_with_rsa_key(publickey, self.text)
        self.assertIsNotNone(encrypted)

    def test_b64_encryption(self):
        encrypted = self.cryptapi.encrypt_with_rsa_key_b64(self.b64_predefined_public, base64.b64encode(self.text))
        self.assertIsNotNone(encrypted)

    def test_decryption(self):
        private_key = RSA.import_key(self.predefined_private, passphrase=self.passphrase)
        decrypted = self.cryptapi.decrypt_with_rsa_key(private_key, self.known_encrypted_text)
        print(decrypted)
        self.assertEqual(decrypted, self.text)

    def test_b64_decryption(self):
        decrypted = self.cryptapi.decrypte_with_rsa_key_b64(self.b64_predefined_private, self.passphrase,
                                                            base64.b64encode(self.known_encrypted_text))
        print(decrypted)
        self.assertEqual(decrypted, self.text_b64)
