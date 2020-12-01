from liuyanban import app
from flask import render_template,redirect,flash,url_for,request
from .models import Tips,db
from .forms import TipForm


@app.route('/',methods=['GET',"POST"])
def index():
    form = TipForm()
    if form.validate_on_submit():

        tip = Tips(poster=form.poster.data,body=form.body.data,posttime=form.posttime.data)
        db.session.add(tip)
        db.session.commit()
        flash("New tip was save success.")
        return redirect(url_for('index'))
    page = request.args.get('page', 2, type=int)
    pagination  = Tips.query.order_by(Tips.posttime.desc()).paginate(page,per_page=10,error_out=False)
    tips = pagination.items

    return render_template("index.html",form = form,tips=tips,pagination=pagination)