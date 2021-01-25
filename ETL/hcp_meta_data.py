sources = [{'name': 'chom', 'url': 'http://bds.hcp.ma/data/1.2.json'},
               {'name': 'demog', 'url': 'http://bds.hcp.ma/data/23.11.json'},
               {'name': 'edu_col_pub', 'url': 'http://bds.hcp.ma/data/6.29.json'},
               {'name': 'edu_lyc_pub', 'url': 'http://bds.hcp.ma/data/6.34.json'},
               {'name': 'edu_lyc_prv', 'url': 'http://bds.hcp.ma/data/6.44.json'}, ]

meta_data = {
    'chom' : {
        'Milieu de rÃ©sidence' : {
            'name' : 'Area',
            'values' : {
                'National' : 'National',
                'Urbain' : 'Urban',
                'Rural' : 'Rural',
            },
            'dtype' : 'str'
        },
        'Groupe d\'Ã¢ges (Emploi)': {
            'name' : 'AgeInterval',
            'values' : {
                '15 ans et plus' : '15+',
                '15-24 ans' : '15-24',
                '25-34 ans' : '25-34',
                '35-44 ans' : '35-44',
                '45-59 ans': '45-59',
                '60 ans et plus': '60+',
            },
            'dtype' : 'str'
        },
        'Sexe' : {
            'name' : 'Gender',
            'values' : {
                'Total' : 'TOT',
                'Masculin': 'MA',
                'Feminin': 'FE',
            },
            'dtype' : 'str'
        },
        'Annee' : {
            'name' : 'Year',
            'dtype': 'int32'
        },
        'Valeur' : {
            'name' : 'Percentage',
            'dtype': 'float32',
            'transform' : lambda x: round(x/100, 5)
        }
    },
    'demog' : {
        'Milieu' : {
            'name' : 'Area',
            'values' : {
                'Total' : 'National',
                'Urbain' : 'Urban',
                'Rural' : 'Rural',
            },
            'dtype' : 'str'
        },
        'Groupe d\'Ã¢ge': {
            'name' : 'AgeInterval',
            'values' : {
                'Total' : 'TOT',
                '75 &+' : '75+',
                '80 &+' : '80+',
            },
            'dtype' : 'str'
        },
        'Sexe' : {
            'name' : 'Gender',
            'values' : {
                'Total' : 'TOT',
                'Masculin': 'MA',
                'Feminin': 'FE',
            },
            'dtype' : 'str'
        },
        'Annee' : {
            'name' : 'Year',
            'dtype': 'int32'
        },
        'Valeur' : {
            'name' : 'Pop',
            'dtype': 'int32',
            'transform' : lambda x: x*1000
        }
    },
    'edu_col_pub' : {
        'Milieu de rÃ©sidence' : {
            'name' : 'Area',
            'values' : {
                'National' : 'National',
                'Urbain' : 'Urban',
                'Rural' : 'Rural',
            },
            'dtype' : 'str'
        },
        'Niveaux secondaire collÃ©gial' : {
            'name' : 'Grade',
            'values' : {
                'Total' : 'TOT',
                '1 Ã¨re annÃ©e' : 'C1',
                '2 Ã¨me annÃ©e' : 'C2',
                '3 Ã¨me annÃ©e' : 'C3',
            },
            'dtype' : 'str'
        },
        'Age (enseignement)': {
            'name' : 'Age',
            'values' : {
                'Total' : 'TOT',
                '10 ans' : '10',
                '11 ans' : '11',
                '12 ans': '12',
                '13 ans': '13',
                '14 ans': '14',
                '15 ans': '15',
                '16 ans': '16',
                '17 ans': '17',
                '18 ans': '18',
                '19 ans': '19',
                '20 ans': '20',
                '21 ans': '21'
            },
            'dtype' : 'str'
        },
        'Sexe' : {
            'name' : 'Gender',
            'values' : {
                'Total' : 'TOT',
                'Feminin': 'FE',
            },
            'dtype' : 'str'
        },
        'Annee' : {
            'name' : 'Year',
            'dtype': 'int32'
        },
        'Valeur' : {
            'name' : 'Number',
            'dtype': 'int32',
            'transform' : lambda x: x
        }
    },
    'edu_lyc_pub' : {
        'Milieu de rÃ©sidence' : {
            'name' : 'Area',
            'values' : {
                'National' : 'National',
                'Urbain' : 'Urban',
                'Rural' : 'Rural',
            },
            'dtype' : 'str'
        },
        'Niveaux secondaire qualifiant' : {
            'name' : 'Grade',
            'values' : {
                'Total' : 'TOT',
                'Tronc commun' : 'L1',
                '1 Ã¨re annÃ©e bac' : 'L2',
                '2 Ã¨me annÃ©e bac' : 'L3',
            },
            'dtype' : 'str'
        },
        'Age (enseignement)': {
            'name' : 'Age',
            'values' : {
                'Total' : 'TOT',
                '14 ans': '14',
                '15 ans': '15',
                '16 ans': '16',
                '17 ans': '17',
                '18 ans': '18',
                '19 ans': '19',
                '20 ans': '20',
                '21 ans': '21',
                '22 ans': '22',
                '23 ans': '23',
                '24 ans et plus': '24+',
            },
            'dtype' : 'str'
        },
        'Sexe' : {
            'name' : 'Gender',
            'values' : {
                'Total' : 'TOT',
                'Feminin': 'FE',
            },
            'dtype' : 'str'
        },
        'Annee' : {
            'name' : 'Year',
            'dtype': 'int32'
        },
        'Valeur' : {
            'name' : 'Number',
            'dtype': 'int32',
            'transform' : lambda x: x
        }
    },
    'edu_lyc_prv': {
        'Niveaux secondaire qualifiant': {
            'name': 'Grade',
            'values': {
                'Total' : 'TOT',
                'Tronc commun' : 'L1',
                '1 Ã¨re annÃ©e bac' : 'L2',
                '2 Ã¨me annÃ©e bac' : 'L3',
            },
            'dtype': 'str'
        },
        'Sexe': {
            'name': 'Gender',
            'values': {
                'Total': 'TOT',
                'Feminin': 'FE',
            },
            'dtype': 'str'
        },
        'Annee': {
            'name': 'Year',
            'dtype': 'int32'
        },
        'Valeur': {
            'name': 'Number',
            'dtype': 'int32',
            'transform': lambda x: x
        }
    },
}