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
            for k in range(0,3):
                db.session.add(Comment('This is '+str(k)+'comment',1+3*i+j,i+1))

    db.session.commit()

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
    user=User.query.get(1)
    print user.images
if __name__=='__main__':
    manager.run()
#