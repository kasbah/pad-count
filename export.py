import pickle
rejected = {
     2: []
    , 3: []
    , 4: []
    , 5: []
    , 6: []
    , 7: []
    , 8: []
}

pickle_path = "rejected.pickle"

rejected['global'] = ['027915a8faa3a17c681fd6d11eb142d7f545569d'
, '19115680fff22d0903606006bee92d8839313df3'
, '1a8ff2613fd1b9e9ec010fec637118cbc9aa1b77'
, '1a9b19742154cf4e86dd8433b4c4186182c027dd'
, '1e3a947645903b248c5e3713289312fc7aed55f6'
, '41471be01916c253ea75a5eb333c202b328d6a8a'
, '42226a028fc23d54575d884be837126b7dae08f5'
, '465b788dfa0eabaa2a212faa6d710aef5eed5b4c'
, '474d8e5f0580bee1924c8f2174d8ed9efff86575'
, '555f86b190f373fef432272bdb92b33141b05873'
, '583b122fd29683f61d0aa1bd63db427635484614'
, '5973249daa2861ba688ec3ad851d805828ae9a08'
, '5d66a9e332acde31d444d90bac0bc0d960cd7bbb'
, '60186505c827bba8509d060cc568161d29c0b833'
, '6470e0a227e4abfd6c44c3f1ddd778a84c375abf'
, '65f6eb96fe2be96436c738c82234a6ee7e9f57d2'
, '6b61dc4ab2d770cb143852db327f316aef67437a'
, '77d729bd440cec3d1a08997a23549591a06cbd80'
, '79056eb5e48637c2f450fe24619e6a2b452c07eb'
, '7ded11c1ae661ccf7e0da5a6881f44e6ffd78bbe'
, '7e7d87082b60562eb6e0d2362bae3432835d866d'
, '7f675e05e93f6253e7bcdae4bfb9f2e9c4a9cae7'
, '7f928b1be5897f475c8464d0d60c6f548b5be33e'
, '846333cea2cd3986d44bb4f315b7c6c70fd3561b'
, '867acbe8a11bb4844f88e7b586d06851bb80c6f2'
, '8727992830eef7b7c9f33391dd6039b62181c7b8'
, '8be210e1f96c1d30b0bac7cedbf2da1514346155'
, '9294da427ffca6c21c41a003b3435b27fee89da9'
, '94a0e4791510dd2f2fe161b06b2efe3e5bf88ded'
, '96c5c7c0dec54db12d59e7bd85262c5aba504cdd'
, 'a63da11857371c9e2f030633c4b366accff1e2e3'
, 'ab53fd1498ee348965ed6205c2c72bded52a9e79'
, 'ba23f9f6f3aec7f603363bb8a11b85dc5c46036f'
, 'ba7a7213e7963f9f1bab83b969610dd04ad086fc'
, 'c11d1b09553611a36267b7b16ffe1bc915823fc4'
, 'd6dc80659465115195bfb8ff8b78ae2fa1dbdd0c'
, 'df13a434a703c1ef7dff68655ff5b242b26c890c'
, 'e15cad7f88655c7359052879f0820b8f3aa559b4'
, 'ec3ce74dbc872f6baf9fb75710b665a4341a9ffa'
, 'f03d107a61be6a51584b80ca82c6cffbcf75d256'
, 'f13729a7294d2510acde5cfc5046a20ec65755b0'
, 'f9d5318a8f2904e44ef8315dc91aa6323702fadc'
, 'f9e76544b01963af2f041e7818c6867406f066cf']

with open(pickle_path, "w") as f:
    pickle.dump(rejected, f)
