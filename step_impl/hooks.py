from getgauge.python import before_scenario, before_step, after_suite


@before_step
def start_step(context):
    print(f"Начинаем шаг: {context.step.text}")


@after_suite
def end_tests():
    print("Все тесты завершены")
