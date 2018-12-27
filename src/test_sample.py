import SlackbotLambda



def test_answer():
    assert SlackbotLambda.lambda_handler({'text':'PyTest event test'}, None)
