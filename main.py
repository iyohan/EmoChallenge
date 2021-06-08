from screens import StartScreen, MainScreen, FeverScreen, MiniChamScreen, EndScreen

def main():
    # init 
    start_screen = StartScreen()
    main_screen = MainScreen()
    fever_screen = FeverScreen()
    mini_cham_screen = MiniChamScreen()
    end_screen = EndScreen()
    
    # testing을 0으로 주면 바로 바로 캡쳐가 됨.
    main_screen.testing = 0
    fever_screen.testing = 0
    
    # game
    main_screen.character, main_screen.difficulty, main_screen.music = start_screen.run()
    fever_screen.character = main_screen.character

    while(1):
        main_ret = main_screen.run()
        if main_ret == 'enter_fever':
            mini_ret = mini_cham_screen.run()
            if mini_ret == 'enter_fever':
                fever_screen.score = main_screen.score
                fever_ret = fever_screen.run()
                main_screen.score = fever_screen.score
                if fever_ret == 'finish':
                    break
            elif mini_ret == 'finish':
                break
        elif main_ret == 'finish':
            break
    end_screen.score = max(main_screen.score, fever_screen.score)
    end_screen.run()
    
if __name__ == '__main__':
    main()