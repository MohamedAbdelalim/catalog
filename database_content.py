from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item, User, Category


engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

user1 = User(name='Ahmed', email='example@example.com', picture="https://yt3.g\
    gpht.com/a-/AAuE7mC5UU5nZGjPi72_SdtOY5vQ5P48\
    i8jveih3YC4S=s88-c-k-c0xffffffff-no-rj-mo")
session.add(user1)
session.commit()

user2 = User(name='Mohamed', email='example1@example.com', picture="https://y\
    t3.ggpht.com/a-/AAuE7mC5UU5nZGjPi72_SdtOY5vQ5P48i8\
    jveih3YC4S=s88-c-k-c0xffffffff-no-rj-mo")
session.add(user2)
session.commit()

category1 = Category(name='Cars')
session.add(category1)
session.commit()

item1 = Item(name='BMW i8', description='The BMW i8 is a plug-in hybrid \
sports car developed by BMW. The i8 is part of BMW\'s electric fl\
eet \"Project i\" being marketed as a new sub-b\
rand, BMW i', category=category1, user=user1)
session.add(item1)
session.commit()

item2 = Item(name='Nissan GT-R', description='The Nissan GT-R is a high-perfo\
rmance sports car produced by Japanese automobile manufacturer Nissan, unvei\
led in 2007.It is the successor to the Nissan Skyline GT-R, although no long\
er part of the Skyline range itself, that name now being used for Nissan\'s lu\
xury-sport market.', category=category1, user=user1)
session.add(item2)
session.commit()

category2 = Category(name='Motorcycles')
session.add(category2)
session.commit()

item3 = Item(name='Harley-Davidson VRSC', description='The Harley-Davidson VR\
SC, or V-Rod, was a line of V-twin muscle bikes, produced by Harley-Davidson f\
rom 2001 until 2017. It is notable as the first Harley-Davidson street motor\
cycle to feature a modern engine with DOHC and liqu\
id cooling', category=category2, user=user1)
session.add(item3)
session.commit()

category3 = Category(name='Bicycles')
session.add(category3)
session.commit()

item4 = Item(name='DOGMA F10', description='Dogma F10 has also inherited mu\
ch from the BOLIDE,currently the fastest bike in the world, the current Hour R\
ecord holder with Sir Bradley Wiggins, time trial World Champion with Kiryen\
ka and winner of Tour de France 2016 with Chris F\
roome.', category=category3, user=user1)
session.add(item4)
session.commit()

category4 = Category(name='Buses')
session.add(category4)
session.commit()

item5 = Item(name='London bus', description='London Buses is the subsidiar\
y of Transport for London that manages bus services within Greater L\
ondon.', category=category4, user=user1)
session.add(item5)
session.commit()

category5 = Category(name='Trains')
session.add(category5)
session.commit()

item6 = Item(name='Bullet train', description='The Shinkansen colloquially kn\
own in English as the bullet train, is a network of high-speed railway line\
s in Japan. Initially, it was built to connect distant Japanese regions with T\
okyo, the capital, in order to aid economic growth and dev\
elopment.', category=category5, user=user2)
session.add(item6)
session.commit()

category6 = Category(name='Ships')
session.add(category6)
session.commit()

item7 = Item(name='Cruise ship', description='A cruise ship is a passenger sh\
ip used for pleasure voyages when the voyage itself, the ship\'s amenities, a\
nd sometimes the different destinations along the way, form part of the pass\
engers\' experience.', category=category6, user=user2)
session.add(item7)
session.commit()

category7 = Category(name='Airplanes')
session.add(category7)
session.commit()

item8 = Item(name='Boeing 737', description='The Boeing 737 MAX is a narr\
ow-body aircraft series manufactured by Boeing Commercial Airplanes as the\
fourth generation of the Boeing 737, succeeding the Boeing 737 Next Gener\
ation', category=category7, user=user2)
session.add(item8)
session.commit()
