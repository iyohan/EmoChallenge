from screens import StartScreen, MainScreen, FeverScreen, MiniChamScreen, EndScreen

def main():
    # init 
    start_screen = StartScreen()
    main_screen = MainScreen()
    fever_screen = FeverScreen()
    mini_cham_screen = MiniChamScreen()
    end_screen = EndScreen()
    
    # testing을 0으로 주면 바로 바로 캡쳐가 됨.
    main_screen.testing = 1
    fever_screen.testing = 1
    
    # game
    main_screen.character, main_screen.difficulty, main_screen.music = start_screen.run()
    fever_screen.character = main_screen.character

    score = 0
    while(1):
        main_ret = main_screen.run()
        score = main_screen.score
        if main_ret == 'enter_fever':
            mini_ret = mini_cham_screen.run()
            if mini_ret == 'enter_fever':
                fever_screen.score = score
                fever_ret = fever_screen.run()
                score = fever_screen.score
                if fever_ret == 'finish':
                    break
            elif mini_ret == 'finish':
                break
        elif main_ret == 'finish':
            break
    end_screen.score = score
    end_screen.run()
    
if __name__ == '__main__':
    main()