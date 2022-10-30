from random import seed
from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import authentication, post, message
from sqlalchemy import exc


# Register blueprint
blueprint = Blueprint('message', __name__, url_prefix='/pm/')


# Return page for messaging
# cur_conversation: user to send message to
@blueprint.route('/message', methods=('GET', 'POST'))
def message_index():
    if not session.get('user_id'):
        flash('Login required.')
        return redirect(url_for('user.login'))
    args = request.args.to_dict()
    cur_user = session.get('user_id')

    if args:
        cur_conversation = args['conversation']
    else:
        cur_conversation = ''
        message_history = ''

    if request.method == 'POST':
        message.send_message(cur_user, cur_conversation,
                             request.form['content'])

    connections = message.get_connections(cur_user)
    message_history = message.get_message_history(
        cur_user, cur_conversation)

    return render_template('message.html', connections=connections,
                           cur_conversation=cur_conversation, message_history=message_history)
