from wtforms import Form, StringField


class YelpSearchForm(Form):
    search = StringField('')