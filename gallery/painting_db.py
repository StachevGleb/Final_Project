# from gallery.models import Artist, Painting
# from gallery import db
#
#
# def save_artist():
#     artist01 = Artist(artistname='Vincent van Gogh',
#                       about='He was a Dutch Post painter, posthumouslybecame one of the most famous and influential.')
#     artist02 = Artist(artistname='Leonardo da Vinci',
#                       about='He was an Italian polymath of the High Renaissance who was active as a painter.')
#     artist03 = Artist(artistname='Pablo Picasso',
#                       about='He was a Spanish painter and theatre designer who spent most of his adult.')
#     artist04 = Artist(artistname='Claude Monet',
#                       about='He was a French painter and founder of impressionist painting who is seen modernism.')
#     artist05 = Artist(artistname='Salvador Dalí',
#                       about='He was a Spanish surrealist artist renowned for his technical skill.')
#     artist06 = Artist(artistname='Michelangelo',
#                       about='He was an Italian sculptor, painter, architect and poet of the High Renaissance.')
#     artist07 = Artist(artistname='Raphael',
#                       about='He was an Italian painter and architect of the High Renaissance. His work is admired for its clarity of form.')
#     artist08 = Artist(artistname='Artemisia Gentileschi',
#                       about='She was an Italian Baroque painter, seventeenth-century artists.')
#     artist09 = Artist(artistname='Rembrandt',
#                       about='He was a Dutch Golden Age painter, printmaker and draughtsman. An innovative and prolific master in three media.')
#     artist10 = Artist(artistname='JMW Turner',
#                       about='He was an English Romantic painter, printmaker and watercolourist. He is known for his expressive colouring.')
#     artist11 = Artist(artistname='Paul Cézanne',
#                       about='He was a French artist and Post-Impressionist painter whose work introduced new modes of representation and influenced avant-garde artistic movements of the early 20th.')
#     artist12 = Artist(artistname='Mary Cassatt',
#                       about='She was an American painter and printmaker. She was born in Allegheny, Pennsylvania (now part of Pittsburgh`s North Side), but lived much of her adult life in France.')
#     artist13 = Artist(artistname='Gustav Klimt',
#                       about='He was an Austrian symbolist painter and one of the most prominent members of the Vienna Secession movement.')
#     artist14 = Artist(artistname='Georgia Totto O`Keeffe',
#                       about='She was an American modernist artist. She was known for her paintings of enlarged flowers, New York skyscrapers.')
#     artist15 = Artist(artistname='Jackson Pollock',
#                       about='He was an American painter and a major figure in the abstract expressionist movement. He was widely noticed for his "drip technique".')
#
#     artists_list = [artist01, artist02, artist03, artist04, artist05, artist06, artist07, artist08, artist09, artist10,
#                     artist11, artist12, artist13, artist14, artist15]
#
#     for x in artists_list:
#         db.session.add(x)
#         db.session.commit()
#
#
# def save_painting():
#     painting01 = Painting(title='Vincent van Gogh',
#                           description='The Starry Night', artist_id=1)
#     painting02 = Painting(title='Vincent van Gogh',
#                           description='The Old Tower in the Fields', artist_id=1)
#     painting03 = Painting(title='Leonardo da Vinci',
#                           description='Ginevra de Benci', artist_id=2)
#     painting04 = Painting(title='Leonardo da Vinci',
#                           description='Self-portrait', artist_id=2)
#     painting05 = Painting(title='Pablo Picasso',
#                           description='Science and Charity', artist_id=3)
#     painting06 = Painting(title='Pablo Picasso',
#                           description='Figures at the Seaside', artist_id=3)
#     painting07 = Painting(title='Claude Monet',
#                           description='Anglers on the Seine at Poissy', artist_id=4)
#     painting08 = Painting(title='Claude Monet',
#                           description='Antibes Seen from the Cape, Mistral Wind', artist_id=4)
#     painting09 = Painting(title='Salvador Dalí',
#                           description='The Persistence of Memory', artist_id=5)
#     painting10 = Painting(title='Salvador Dalí',
#                           description='The Disintegration of the Persistence of Memory', artist_id=5)
#     painting11 = Painting(title='Michelangelo',
#                           description='The Torment of Saint Anthony', artist_id=6)
#     painting12 = Painting(title='Michelangelo',
#                           description='The Creation of Adam', artist_id=6)
#     painting13 = Painting(title='Raphael',
#                           description='The Three Graces', artist_id=7)
#     painting14 = Painting(title='Raphael',
#                           description='The School of Athens', artist_id=7)
#     painting15 = Painting(title='Artemisia Gentileschi',
#                           description='Self Portrait as Saint Catherine of Alexandria', artist_id=8)
#     painting16 = Painting(title='Artemisia Gentileschi',
#                           description='Cleopatra', artist_id=8)
#     painting17 = Painting(title='Rembrandt',
#                           description='The Night Watch', artist_id=9)
#     painting18 = Painting(title='Rembrandt',
#                           description='The Baptism of the Eunuch', artist_id=9)
#     painting19 = Painting(title='JMW Turner',
#                           description='Fishermen at Sea', artist_id=10)
#     painting20 = Painting(title='JMW Turner',
#                           description='Moonlight, a Study at Millbank', artist_id=10)
#     painting21 = Painting(title='Paul Cézanne',
#                           description='Academic Nude', artist_id=11)
#     painting22 = Painting(title='Paul Cézanne',
#                           description='Farmyard', artist_id=11)
#     painting23 = Painting(title='Mary Cassatt',
#                           description='Picking flowers in a field', artist_id=12)
#     painting24 = Painting(title='Mary Cassatt',
#                           description='Lilacs in a Window', artist_id=12)
#     painting25 = Painting(title='Gustav Klimt',
#                           description='Old Burgtheater in Vienna', artist_id=13)
#     painting26 = Painting(title='Gustav Klimt',
#                           description='Sappho', artist_id=13)
#     painting27 = Painting(title='Georgia Totto O`Keeffe',
#                           description='Blue and Green Music', artist_id=14)
#     painting28 = Painting(title='Georgia Totto O`Keeffe',
#                           description='White Hollyhock and Little Hills', artist_id=14)
#     painting29 = Painting(title='Jackson Pollock',
#                           description='Lavender Mist', artist_id=15)
#     painting30 = Painting(title='Jackson Pollock',
#                           description='The She Wolf', artist_id=15)
#
#     artists_list = [painting01, painting02, painting03, painting04, painting05, painting06,
#                     painting07, painting08, painting09, painting10, painting11, painting12, painting13,
#                     painting14, painting15, painting16, painting17, painting18, painting19,
#                     painting20, painting21, painting22, painting23, painting24, painting25, painting26,
#                     painting27, painting28, painting29, painting30]
#
#     for x in artists_list:
#         db.session.add(x)
#         db.session.commit()

# ##################################list of artist - paintings uploading################################
#
#
# paintings = [
#     {
#         'creator': 'Vincent van Gogh',
#         'title': 'The Starry Night',
#         'description': 'Oil on canvas by Vincent van Gogh, 1889; in the Museum of Modern Art, New York City.'
#     },
#     {
#         'creator': 'Vincent van Gogh',
#         'title': 'The Old Tower in the Fields',
#         'description': 'Oil on canvas on cardboard by Vincent van Gogh, 1884.'
#     },
#     {
#         'creator': 'Leonardo da Vinci',
#         'title': 'Ginevra de Benci',
#         'description': 'Courtesy National Gallery of Art, Washington.'
#     },
#     {
#         'creator': 'Leonardo da Vinci',
#         'title': 'Self-portrait',
#         'description': 'Long regarded as a self-portrait, the red chalk drawing of an old man.'
#     },
#     {
#         'creator': 'Pablo Picasso',
#         'title': 'Science and Charity',
#         'description': 'One of the major works from Picasso’s early years of training.'
#     },
#     {
#         'creator': 'Pablo Picasso',
#         'title': 'Figures at the Seaside',
#         'description': 'Neoclassicist & Surrealist Period, 1931.'
#     }, {
#         'creator': 'Claude Monet',
#         'title': 'Anglers on the Seine at Poissy',
#         'description': 'Impressionism, Belvedere, Vienna, Austria, 1882.'
#     },
#     {
#         'creator': 'Claude Monet',
#         'title': 'Antibes Seen from the Cape, Mistral Wind',
#         'description': 'Impressionism, Antibes, 1888.'
#     }, {
#         'creator': 'Salvador Dalí',
#         'title': 'The Persistence of Memory',
#         'description': 'One of the most iconic and recognizable paintings of Surrealism.'
#     },
#     {
#         'creator': 'Salvador Dalí',
#         'title': 'The Disintegration of the Persistence of Memory',
#         'description': 'Dali repeated his theme of the melting watches many times, most notably in the 1950’s.'
#     }
# ]
#
# #################################end of artist - paintings uploading##################################
#
#
#
#
# artists = [
#     {
#         'artistname': 'Vincent van Gogh',
#         'about': 'He was a Dutch Post-Impressionist painter who posthumously became one of the most famous and influential.',
#     },
#     {
#         'artistname': 'Leonardo da Vinci',
#         'about': 'He was an Italian polymath of the High Renaissance who was active as a painter.',
#     },
#     {
#         'artistname': 'Pablo Picasso',
#         'about': 'He was a Spanish painter, sculptor, printmaker, ceramicist and theatre designer who spent most of his adult.',
#     },  {
#         'artistname': 'Claude Monet',
#         'about': 'He was a French painter and founder of impressionist painting who is seen as a key precursor to modernism.',
#     },
#     {
#         'artistname': 'Salvador Dalí',
#         'about': 'He was a Spanish surrealist artist renowned for his technical skill.',
#     },
# {
#         'artistname': 'Michelangelo',
#         'about': 'He was an Italian sculptor, painter, architect and poet of the High Renaissance.',
#     },
#     {
#         'artistname': 'Raphael',
#         'about': 'He was an Italian painter and architect of the High Renaissance. His work is admired for its clarity of form.',
#     },
#     {
#         'artistname': 'Artemisia Gentileschi',
#         'about': 'She was an Italian Baroque painter. Gentileschi is considered among the most accomplished seventeenth-century artists.',
#     },  {
#         'artistname': 'Rembrandt',
#         'about': 'He was a Dutch Golden Age painter, printmaker and draughtsman. An innovative and prolific master in three media.',
#     },
#     {
#         'artistname': 'JMW Turner',
#         'about': 'He was an English Romantic painter, printmaker and watercolourist. He is known for his expressive colouring.',
#     },
# {
#         'artistname': 'Paul Cézanne',
#         'about': 'He was a French artist and Post-Impressionist painter whose work introduced new modes of representation and influenced avant-garde artistic movements of the early 20th.',
#     },
#     {
#         'artistname': 'Mary Cassatt',
#         'about': 'She was an American painter and printmaker. She was born in Allegheny, Pennsylvania (now part of Pittsburgh`s North Side), but lived much of her adult life in France.',
#     },
#     {
#         'artistname': 'Gustav Klimt',
#         'about': 'He was an Austrian symbolist painter and one of the most prominent members of the Vienna Secession movement.',
#     },
#     {
#         'artistname': 'Georgia Totto O`Keeffe',
#         'about': 'She was an American modernist artist. She was known for her paintings of enlarged flowers, New York skyscrapers.',
#     },
#     {
#         'artistname': 'Jackson Pollock',
#         'about': 'He was an American painter and a major figure in the abstract expressionist movement. He was widely noticed for his "drip technique".',
#     }
# ]
#
#
