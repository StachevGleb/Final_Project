# from gallery.models import Artist, Painting
# from gallery import db
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
#
#     artists_list = [artist01, artist02, artist03, artist04, artist05]
#
#     for x in artists_list:
#         db.session.add(x)
#         db.session.commit()

# def save_painting():
#     painting01 = Painting(title='Vincent van Gogh',
#                       description='The Starry Night', artist_id=1)
#     painting02 = Painting(title='Vincent van Gogh',
#                       description='The Old Tower in the Fields', artist_id=1)
#     painting03 = Painting(title='Leonardo da Vinci',
#                       description='Ginevra de Benci', artist_id=2)
#     painting04 = Painting(title='Leonardo da Vinci',
#                       description='Self-portrait', artist_id=2)
#     painting05 = Painting(title='Pablo Picasso',
#                       description='Science and Charity', artist_id=3)
#     painting06 = Painting(title='Pablo Picasso',
#                       description='Figures at the Seaside', artist_id=3)
#     painting07 = Painting(title='Claude Monet',
#                       description='Anglers on the Seine at Poissy', artist_id=4)
#     painting08 = Painting(title='Claude Monet',
#                       description='Antibes Seen from the Cape, Mistral Wind', artist_id=4)
#     painting09 = Painting(title='Salvador Dalí',
#                       description='The Persistence of Memory', artist_id=5)
#     painting10 = Painting(title='Salvador Dalí',
#                       description='The Disintegration of the Persistence of Memory', artist_id=5)
#
#     artists_list = [painting01, painting02, painting03, painting04, painting05, painting06, painting07, painting08, painting09, painting10]
#
#     for x in artists_list:
#         db.session.add(x)
#         db.session.commit()
#
#



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
#     }
# ]
#
#
