class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int eSum = 0;
        for(int i=0;i<energy.size();i++){
            eSum= eSum + energy[i];
        }
        
        int tEnergy;
        int ExperienceNeeded = initialExperience;
        int f=0;
        if(initialEnergy>eSum){
            tEnergy = 0;
        }
        else{
           tEnergy = eSum+1-initialEnergy;
        }
        
        for(int i=0;i<experience.size();i++){
            if(ExperienceNeeded>experience[i]){
                ExperienceNeeded+=experience[i];
                continue;
            }else{
                ExperienceNeeded++;
                f++;
                i--;
            }
        }
        
        int training = f+tEnergy;
        return training;
        
    }
};