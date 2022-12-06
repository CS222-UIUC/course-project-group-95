from flask import flash, redirect, render_template, request, Blueprint, url_for, session
from ..models import message


# Register blueprint
blueprint = Blueprint('message', __name__, url_prefix='/pm/')


# Return page for messaging
# cur_conversation: user to send message to
# Login required, or will redirect to login page
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

    if request.method == 'POST':
        message.send_message(cur_user, cur_conversation,
                             request.form['content'])

    connections = message.get_connections(cur_user)
    message_history = message.get_message_history(
        cur_user, cur_conversation)

    return render_template('message.html', connections=connections,
                           cur_conversation=cur_conversation, message_history=message_history)


# Return page for connection management
@blueprint.route('/connection_management', methods=('GET', 'POST'))
def connection_management():
    cur_user = session.get('user_id')
    search_result = ""

    if request.method == 'POST':
        dict = request.form.to_dict()

        # For searching user
        if "username" in dict.keys():
            username = dict['username']
            find = message.search_user(username)
            connections = message.get_connections(cur_user)
            connection_exist = False
            for connection in connections:
                if connection.username == username:
                    connection_exist = True

            if len(find) != 1 or find[0].username == cur_user:
                flash('No matching result')
            elif connection_exist:
                flash('User already connected')
            else:
                search_result = find[0]

        # For sending connection request to the searched user
        elif "send_connection" in dict.keys():
            username = dict['send_connection']
            if message.check_request_exist(cur_user, username):
                flash('Connection request already exist')
            else:
                message.send_connection_request(cur_user, username)
                flash('Connection request sent')

        # For accepting a received pending connection request
        elif "accept_connection" in dict.keys():
            print('accc')
            username = dict['accept_connection']
            message.add_connection(username, cur_user)
            message.delete_connection_request(username, cur_user)

        # For declining a received pending connection request
        elif "decline_connection" in dict.keys():
            username = dict['decline_connection']
            message.delete_connection_request(username, cur_user)

        # For deleting a current existing connection
        elif "delete_connection" in dict.keys():
            username = dict['delete_connection']
            message.delete_connection(username, cur_user)

    connections = message.get_connections(cur_user)
    pending_sent_request = message.get_pending_sent_request(cur_user)
    pending_received_request = message.get_pending_received_request(cur_user)

    return render_template('connection.html', connections=connections, pending_sent_request=pending_sent_request,
                           search_result=search_result, pending_received_request=pending_received_request)
