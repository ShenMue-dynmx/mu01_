import ikpy.chain
import mimimodules.POSTjson as pst
import mimimodules.mousepos as mc


#jnt=["link_Cylinder","link_Cube.001","link_Cube.002","link_Cube.003"]
screenWidth,screenHeight=mc.screenSpec()
def SolveAndPost(targ,doPost=False):
    arm_angles=my_chain.inverse_kinematics(targ)
    fi=arm_angles[1:-1:1]
    if(doPost):
        pst.post(["link_Cylinder", "link_Cube.001", "link_Cube.002", "link_Cube.003"], fi )
    return fi

armFile="/home/shenmu/DevStuff/urdfs/robotarm2/urdf/arm.urdf"
my_chain = ikpy.chain.Chain.from_urdf_file(armFile,base_elements=("link_base",))
target_position = [0.5,0.3, 2]

#print("The angles of each joints are : ", )


while(1):
    z=(screenHeight-mc.getMouse().y)/screenHeight *3
    x=(screenWidth-mc.getMouse().x)/screenWidth*6 -3
    target_position=[x,0,z]
    SolveAndPost(target_position,True)

