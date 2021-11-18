import click
from app import app, db
from app.models import Message

@app.cli.command('hello')
@click.option('--count', default=20, help="添加留言数据，默认为20")
def forge(count):
    """生成虚拟数据"""
    from faker import Faker
    
    db.drop_all()
    db.create_all()
    
    fake = Faker('zh_CN')
    click.echo('添加中...')
    
    for i in range(count):
        message = Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('添加了%d条数据' % count)
    