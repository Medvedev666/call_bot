import json
from .call_config import webhook_url

def get_data_dict(
        apiKey: str, phone: str, gender: bool,
        doctor: str, full_name: str, data_birth: str,
        insurance_name: str, insurance_number: str,
        comfort_date: str, my_phone, user_id

    ):

    my_phone = f'{phone[0]}, {phone[1:4]}, {phone[4:7]}, {phone[7:9]}, {phone[9:]}'

    user_id = str(user_id)

    data = {
    "apiKey": apiKey,
    "phone": phone,
    "dutyPhone": "1",
    "needRecording": 1,
    "endWebhook": 1,
    "webhookUrl": webhook_url,
    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"звонок завершен\"}",
    "webhookHeaders": "{}",
    "record": {
        "text": f"Добрый день! Я хочу записаться на прием к {doctor} по ДМС",
        "gender": gender
    },
    "ivrs": [
        {
        "keyWords": "здраствуйте|добрый день|приветствуем|добро пожаловать|доброе утро|добрый вечер",
        "record": {
            "source": "text",
            "text": f"Я хочу записаться на прием к {doctor} по ДМС",
            "gender": gender

        },
        "id": 51,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "ваше имя|фамилия|отчесвто|вас зовут|фио|имя",
            "record": {
                "source": "text",
                "text": full_name,
                "gender": gender
            },
            "id": 52,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "дата рождения|кода родились|возраст|день рождения",
                "record": {
                    "source": "text",
                    "text": f"родился {data_birth}",
                    "gender": gender
                },
                "id": 53,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "страховую|страховая|страховщик|номер дмс|номер полиса|компания|страховой агент|застрахованы|полис",
                    "record": {
                        "source": "text",
                        "text": f"страховая: {insurance_name}, номер полиса: {insurance_number}",
                        "gender": gender
                    },
                    "id": 54,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
                        "record": {
                            "source": "text",
                            "text": f"номер телефона: {my_phone}",
                            "gender": gender
                        },
                        "id": 55,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
                            "record": {
                                "source": "text",
                                "text": f"к {doctor}",
                                "gender": gender
                            },
                            "id": 56,
                            "recognize": 1,
                            "ivrs": [
                                {
                                "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
                                "record": {
                                    "source": "text",
                                    "text": f"хочу записаться на {comfort_date}",
                                    "gender": gender
                                },
                                "id": 57,
                                "recognize": 1,
                                "ivrs": [
                                    {
                                    "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                                    "record": {
                                        "source": "text",
                                        "text": "хорошо, запишите пожалуйста",
                                        "gender": gender
                                    },
                                    "id": 58,
                                    "recognize": 1,
                                    "ivrs": [
                                        {
                                        "keyWords": "записали|добавили|внесла",
                                        "record": {
                                            "source": "text",
                                            "text": "Хорошо, спасибо, до свидания",
                                            "gender": gender
                                        },
                                        "webhookUrl": webhook_url,
                                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                                        "webhookHeaders": "{}",
                                        "id": 59,
                                        "recognize": 1,
                                        "ivrs": []
                                        }
                                    ]
                                    },
                                    {
                                    "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                                    "timeout": 15,
                                    "record": {
                                        "source": "text",
                                        "text": "а на какое времхочу записаться я и на какие даты",
                                        "gender": gender
                                    },
                                    "id": 60,
                                    "recognize": 1,
                                    "ivrs": [
                                        {
                                        "anyWord": 1,
                                        "record": {
                                            "source": "text",
                                            "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                                            "gender": gender
                                        },
                                        "webhookUrl": webhook_url,
                                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                                        "webhookHeaders": "{}",
                                        "id": 61,
                                        "recognize": 1,
                                        "ivrs": []
                                        }
                                    ]
                                    }
                                ]
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },
            
        ]
        },
        
        {
        "keyWords": "ваше имя|фамилия|отчесвто|вас зовут|фио|имя",
        "record": {
            "source": "text",
            "text": full_name,
            "gender": gender
        },
        "id": 1,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "дата рождения|кода родились|возраст|день рождения",
            "record": {
                "source": "text",
                "text": f"родился {data_birth}",
                "gender": gender
            },
            "id": 31,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "страховую|страховая|страховщик|номер дмс|номер полиса|компания|страховой агент|застрахованы|полис",
                "record": {
                    "source": "text",
                    "text": f"страховая: {insurance_name}, номер полиса: {insurance_number}",
                    "gender": gender
                },
                "id": 32,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
                    "record": {
                        "source": "text",
                        "text": f"номер телефона: {my_phone}",
                        "gender": gender
                    },
                    "id": 33,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту|кому|прием|врачу|записаться",
                        "record": {
                            "source": "text",
                            "text": f"к {doctor}",
                            "gender": gender
                        },
                        "id": 34,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "keyWords": "на какую дату записать|когда зписать|на какую дату|дата записи|на какой день|записаться",
                            "record": {
                                "source": "text",
                                "text": f"хочу записаться на {comfort_date}",
                                "gender": gender
                            },
                            "id": 35,
                            "recognize": 1,
                            "ivrs": [
                                {
                                "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                                "record": {
                                    "source": "text",
                                    "text": "хорошо, запишите пожалуйста",
                                    "gender": gender
                                },
                                "id": 36,
                                "recognize": 1,
                                "ivrs": [
                                    {
                                    "keyWords": "записали|добавили|внесла",
                                    "record": {
                                        "source": "text",
                                        "text": "Хорошо, спасибо, до свидания",
                                        "gender": gender
                                    },
                                    "webhookUrl": webhook_url,
                                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                                    "webhookHeaders": "{}",
                                    "id": 37,
                                    "recognize": 1,
                                    "ivrs": []
                                    }
                                ]
                                },
                                {
                                "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                                "timeout": 15,
                                "record": {
                                    "source": "text",
                                    "text": "а на какое времхочу записаться я и на какие даты",
                                    "gender": gender
                                },
                                "id": 38,
                                "recognize": 1,
                                "ivrs": [
                                    {
                                    "anyWord": 1,
                                    "record": {
                                        "source": "text",
                                        "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                                        "gender": gender
                                    },
                                    "webhookUrl": webhook_url,
                                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                                    "webhookHeaders": "{}",
                                    "id": 39,
                                    "recognize": 1,
                                    "ivrs": []
                                    }
                                ]
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },

            {
            "keyWords": "на какую дату записать|когда зписать|на какую дату|дата записи|на какой день|записаться",
            "record": {
                "source": "text",
                "text": f"хочу записаться на {comfort_date}",
                "gender": gender
            },
            "id": 62,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                "record": {
                    "source": "text",
                    "text": "хорошо, запишите пожалуйста",
                    "gender": gender
                },
                "id": 63,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "записали|добавили|внесла",
                    "record": {
                        "source": "text",
                        "text": "Хорошо, спасибо, до свидания",
                        "gender": gender
                    },
                    "webhookUrl": webhook_url,
                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                    "webhookHeaders": "{}",
                    "id": 64,
                    "recognize": 1,
                    "ivrs": []
                    }
                ]
                },
                {
                "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                "timeout": 15,
                "record": {
                    "source": "text",
                    "text": "а на какое времхочу записаться я и на какие даты",
                    "gender": gender
                },
                "id": 65,
                "recognize": 1,
                "ivrs": [
                    {
                    "anyWord": 1,
                    "record": {
                        "source": "text",
                        "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                        "gender": gender
                    },
                    "webhookUrl": webhook_url,
                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                    "webhookHeaders": "{}",
                    "id": 66,
                    "recognize": 1,
                    "ivrs": []
                    }
                ]
                }
            ]
            }
        ]
        },
        {
        "keyWords": "дата рождения|кода родились|возраст|день рождения",
        "record": {
            "source": "text",
            "text": f"родился {data_birth}",
            "gender": gender
        },
        "id": 3,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "страховую|страховая|страховщик|номер дмс|номер полиса|компания|страховой агент|застрахованы|полис",
            "record": {
                "source": "text",
                "text": f"страховая: {insurance_name}, номер полиса: {insurance_number}",
                "gender": gender
            },
            "id": 23,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
                "record": {
                    "source": "text",
                    "text": f"номер телефона: {my_phone}",
                    "gender": gender
                },
                "id": 24,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
                    "record": {
                        "source": "text",
                        "text": f"к {doctor}",
                        "gender": gender
                    },
                    "id": 25,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
                        "record": {
                            "source": "text",
                            "text": f"хочу записаться на {comfort_date}",
                            "gender": gender
                        },
                        "id": 26,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                            "record": {
                                "source": "text",
                                "text": "хорошо, запишите пожалуйста",
                                "gender": gender
                            },
                            "id": 27,
                            "recognize": 1,
                            "ivrs": [
                                {
                                "keyWords": "записали|добавили|внесла",
                                "record": {
                                    "source": "text",
                                    "text": "Хорошо, спасибо, до свидания",
                                    "gender": gender
                                },
                                "webhookUrl": webhook_url,
                                "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                                "webhookHeaders": "{}",
                                "id": 28,
                                "recognize": 1,
                                "ivrs": []
                                }
                            ]
                            },
                            {
                            "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                            "timeout": 15,
                            "record": {
                                "source": "text",
                                "text": "а на какое времхочу записаться я и на какие даты",
                                "gender": gender
                            },
                            "id": 29,
                            "recognize": 1,
                            "ivrs": [
                                {
                                "anyWord": 1,
                                "record": {
                                    "source": "text",
                                    "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                                    "gender": gender
                                },
                                "webhookUrl": webhook_url,
                                "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                                "webhookHeaders": "{}",
                                "id": 30,
                                "recognize": 1,
                                "ivrs": []
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            }
        ]
        },
        {
        "keyWords": "страховую|страховая|страховщик|номер дмс|номер полиса|компания|страховой агент|застрахованы|полис",
        "record": {
            "source": "text",
            "text": f"страховая: {insurance_name}, номер полиса: {insurance_number}",
            "gender": gender
        },
        "id": 4,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
            "record": {
                "source": "text",
                "text": f"номер телефона: {my_phone}",
                "gender": gender
            },
            "id": 16,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
                "record": {
                    "source": "text",
                    "text": f"к {doctor}",
                    "gender": gender
                },
                "id": 17,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
                    "record": {
                        "source": "text",
                        "text": f"хочу записаться на {comfort_date}",
                        "gender": gender
                    },
                    "id": 18,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                        "record": {
                            "source": "text",
                            "text": "хорошо, запишите пожалуйста",
                            "gender": gender
                        },
                        "id": 19,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "keyWords": "записали|добавили|внесла",
                            "record": {
                                "source": "text",
                                "text": "Хорошо, спасибо, до свидания",
                                "gender": gender
                            },
                            "webhookUrl": webhook_url,
                            "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                            "webhookHeaders": "{}",
                            "id": 20,
                            "recognize": 1,
                            "ivrs": []
                            }
                        ]
                        },
                        {
                        "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                        "timeout": 15,
                        "record": {
                            "source": "text",
                            "text": "а на какое времхочу записаться я и на какие даты",
                            "gender": gender
                        },
                        "id": 21,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "anyWord": 1,
                            "record": {
                                "source": "text",
                                "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                                "gender": gender
                            },
                            "webhookUrl": webhook_url,
                            "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                            "webhookHeaders": "{}",
                            "id": 22,
                            "recognize": 1,
                            "ivrs": []
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            }
        ]
        },
        {
        "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
        "record": {
            "source": "text",
            "text": f"номер телефона: {my_phone}",
            "gender": gender
        },
        "id": 4,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
            "record": {
                "source": "text",
                "text": f"к {doctor}",
                "gender": gender
            },
            "id": 10,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
                "record": {
                    "source": "text",
                    "text": f"хочу записаться на {comfort_date}",
                    "gender": gender
                },
                "id": 11,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                    "record": {
                        "source": "text",
                        "text": "хорошо, запишите пожалуйста",
                        "gender": gender
                    },
                    "id": 12,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "записали|добавили|внесла",
                        "record": {
                            "source": "text",
                            "text": "Хорошо, спасибо, до свидания",
                            "gender": gender
                        },
                        "webhookUrl": webhook_url,
                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                        "webhookHeaders": "{}",
                        "id": 13,
                        "recognize": 1,
                        "ivrs": []
                        }
                    ]
                    },
                    {
                    "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                    "timeout": 15,
                    "record": {
                        "source": "text",
                        "text": "а на какое времхочу записаться я и на какие даты",
                        "gender": gender
                    },
                    "id": 14,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "anyWord": 1,
                        "record": {
                            "source": "text",
                            "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                            "gender": gender
                        },
                        "webhookUrl": webhook_url,
                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                        "webhookHeaders": "{}",
                        "id": 15,
                        "recognize": 1,
                        "ivrs": []
                        }
                    ]
                    }
                ]
                }
            ]
            }
        ]
        },
        {
        "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
        "record": {
            "source": "text",
            "text": f"к {doctor}",
            "gender": gender
        },
        "id": 5,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
            "record": {
                "source": "text",
                "text": f"хочу записаться на {comfort_date}",
                "gender": gender
            },
            "id": 5,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                "record": {
                    "source": "text",
                    "text": "хорошо, запишите пожалуйста",
                    "gender": gender
                },
                "id": 6,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "записали|добавили|внесла",
                    "record": {
                        "source": "text",
                        "text": "Хорошо, спасибо, до свидания",
                        "gender": gender
                    },
                    "webhookUrl": webhook_url,
                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                    "webhookHeaders": "{}",
                    "id": 7,
                    "recognize": 1,
                    "ivrs": []
                    }
                ]
                },
                {
                "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                "timeout": 15,
                "record": {
                    "source": "text",
                    "text": "а на какое времхочу записаться я и на какие даты",
                    "gender": gender
                },
                "id": 8,
                "recognize": 1,
                "ivrs": [
                    {
                    "anyWord": 1,
                    "record": {
                        "source": "text",
                        "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                        "gender": gender
                    },
                    "webhookUrl": webhook_url,
                    "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                    "webhookHeaders": "{}",
                    "id": 9,
                    "recognize": 1,
                    "ivrs": []
                    }
                ]
                }
            ]
            },
            {
            "keyWords": "ваше имя|фамилия|отчесвто|вас зовут|фио|имя",
            "record": {
                "source": "text",
                "text": full_name,
                "gender": gender
            },
            "id": 40,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "дата рождения|кода родились|возраст|день рождения",
                "record": {
                    "source": "text",
                    "text": f"родился {data_birth}",
                    "gender": gender
                },
                "id": 41,
                "recognize": 1,
                "ivrs": [
                    {
                    "keyWords": "страховую|страховая|страховщик|номер дмс|номер полиса|компания|страховой агент|застрахованы|полис",
                    "record": {
                        "source": "text",
                        "text": f"страховая: {insurance_name}, номер полиса: {insurance_number}",
                        "gender": gender
                    },
                    "id": 42,
                    "recognize": 1,
                    "ivrs": [
                        {
                        "keyWords": "номер телефона|контактный номер|продктуйте ваш номер|мобильный телефон|номер мобильного",
                        "record": {
                            "source": "text",
                            "text": f"номер телефона: {my_phone}",
                            "gender": gender
                        },
                        "id": 43,
                        "recognize": 1,
                        "ivrs": [
                            {
                            "keyWords": "к кому хотите записаться|какому врачу|кому на прием|какой специалист|какому специалисту",
                            "record": {
                                "source": "text",
                                "text": f"к {doctor}",
                                "gender": gender
                            },
                            "id": 44,
                            "recognize": 1,
                            "ivrs": [
                                {
                                "keyWords": "на какую дату записать|когда зпписать|на какую дату|дата записи|на какой день",
                                "record": {
                                    "source": "text",
                                    "text": f"хочу записаться на {comfort_date}",
                                    "gender": gender
                                },
                                "id": 45,
                                "recognize": 1,
                                "ivrs": [
                                    {
                                    "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
                                    "record": {
                                        "source": "text",
                                        "text": "хорошо, запишите пожалуйста",
                                        "gender": gender
                                    },
                                    "id": 46,
                                    "recognize": 1,
                                    "ivrs": [
                                        {
                                        "keyWords": "записали|добавили|внесла",
                                        "record": {
                                            "source": "text",
                                            "text": "Хорошо, спасибо, до свидания",
                                            "gender": gender
                                        },
                                        "webhookUrl": webhook_url,
                                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                                        "webhookHeaders": "{}",
                                        "id": 47,
                                        "recognize": 1,
                                        "ivrs": []
                                        }
                                    ]
                                    },
                                    {
                                    "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
                                    "timeout": 15,
                                    "record": {
                                        "source": "text",
                                        "text": "а на какое времхочу записаться я и на какие даты",
                                        "gender": gender
                                    },
                                    "id": 48,
                                    "recognize": 1,
                                    "ivrs": [
                                        {
                                        "anyWord": 1,
                                        "record": {
                                            "source": "text",
                                            "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                                            "gender": gender
                                        },
                                        "webhookUrl": webhook_url,
                                        "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                                        "webhookHeaders": "{}",
                                        "id": 49,
                                        "recognize": 1,
                                        "ivrs": []
                                        }
                                    ]
                                    }
                                ]
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            }
        ]
        },
        {
        "keyWords": "на какую дату записать|когда зписать|на какую дату|дата записи|на какой день|в какое время|время приема|дату приема|время",
        "record": {
            "source": "text",
            "text": f"хочу записаться на {comfort_date}",
            "gender": gender
        },
        "id": 6,
        "recognize": 1,
        "ivrs": [
            {
            "keyWords": "да|ага|угу|допустим|возможно|ладно|интересно|хорошо|вроде да|точно|окей|может быть|ну да|еще да|пока да|верно|как раз|актуально|дада|ну да|конечно|естественно|разумеется|скорее|давай|давайте|можно|хочу|согласен|согласна|ещё|хотела бы|хотел бы|ну и",
            "record": {
                "source": "text",
                "text": "хорошо, запишите пожалуйста",
                "gender": gender
            },
            "id": 7,
            "recognize": 1,
            "ivrs": [
                {
                "keyWords": "записали|добавили|внесла",
                "record": {
                    "source": "text",
                    "text": "Хорошо, спасибо, до свидания",
                    "gender": gender
                },
                "webhookUrl": webhook_url,
                "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Записали на выбранную дату\"}",
                "webhookHeaders": "{}",
                "id": 5,
                "recognize": 1,
                "ivrs": []
                }
            ]
            },
            {
            "keyWords": "нет|неа|не|не надо|не хочу|не могу|не нужно|не интересно|не актуально|больше не|никогда|данет|уже нет|сейчас не|уже не|сейчас нет|не интересуюсь|не интересует|до свидания|нет спасибо|спасибо не|ничем|ничего|хватит|неверно",
            "timeout": 15,
            "record": {
                "source": "text",
                "text": "а на какое времхочу записаться я и на какие даты",
                "gender": gender
            },
            "id": 8,
            "recognize": 1,
            "ivrs": [
                {
                "anyWord": 1,
                "record": {
                    "source": "text",
                    "text": "Хорошо, спасибо, проверю свою расписание и перезвоню попозже. До свидания",
                    "gender": gender
                },
                "webhookUrl": webhook_url,
                "webhookParameters": "{\"id\":\"" + user_id + "\",\"result\":\"Не удалось записаться на выбранную дату\"}",
                "webhookHeaders": "{}",
                "id": 5,
                "recognize": 1,
                "ivrs": []
                }
            ]
            }
        ]
        }
    ],
    "endOfSpeech": 1,
    "voiceDetection": 1,
    "answerTimeout": 60,
    }

    return data