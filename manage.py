# -*- encoding=UTF-8 -*-

from mystagram import app,db
from flask_script import Manager
from mystagram.models import User,Image,Comment
import random
from sqlalchemy import or_,and_

manager=Manager(app)

def get_image_url():
    return 'https://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'
@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i+1),'a'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_image_url(),i+1))

    for k in range(1,301):
        for h in range(0,3):
            db.session.add(Comment('This is '+str(h)+'comment',k,random.randint(1,100)))

    db.session.commit()
@manager.command
def pp():
    for i in range(0,3):
        print i
@manager.command
def sp():
    #print 1, User.query.all()
    #print 2,User.query.get(12)
    #print User.query.filter_by(id=5).first()
    #print User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    #print User.query.filter(User.username.endswith('0')).limit(3).all()
    #print User.query.filter(or_(User.id==88,User.id==99)).all()
    #print User.query.filter(and_(User.id >88, User.id < 99)).first_or_404()
    #分页
    #print User.query.order_by(User.id.desc()).paginate(page=1,per_page=10).items
    #user=User.query.get(1)
    #print user.images
    image=Image.query.get(1)
    print image.user

@manager.command
def up():
    for i in range(50,100,2):
        user=User.query.get(i)
        user.username='[New2]'+user.username
    #db.session.commit()
    for i in range(11,20):
         User.query.filter_by(id=i).update({'username':'[New3]'+User.query.get(i).username})
    db.session.commit()
@manager.command
def dele():
    for i in range(50,100,2):
        comment=Comment.query.get(i)
        db.session.delete(comment)
    db.session.commit()

if __name__=='__main__':
    manager.run()
#