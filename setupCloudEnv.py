import os
import subprocess as sp

class util:
    @staticmethod
    def UpdateAndUpgrade():
        aptUpdate: str = """sudo apt update && sudo apt upgrade -y"""
        sp.run(aptUpdate, shell=True)


# Starship CLI Prompt
class cli:
    @staticmethod
    def setupStarship():
        util.UpdateAndUpgrade()
        starshipSetup: str = """curl -sS https://starship.rs/install.sh | sh -s -- -y && echo 'eval "$(starship init bash)"' >> ~/.bashrc"""
        sp.run(starshipSetup, shell=True)


    @staticmethod
    def aptInstall(packagesToGet: list[str]):
        packages: list[str] = ["sudo", "apt", "install"]
        packages.extend(packagesToGet)
        packages.append("-y")

        sp.run(packages, shell=False)

    @staticmethod
    def startFish():
        setFishConfig = """echo 'starship init fish | source' >> ~/.config/fish/config.fish"""
        sp.run(setFishConfig, shell=True)

        # Py Interpreter Is Replaced With This
        os.execlp("fish", "fish")



if __name__ == "__main__":
    packagesToGet: list[str] = ["fish", "btop"]

    cli.setupStarship()

    cli.aptInstall(packagesToGet)

    cli.startFish()
    

    

