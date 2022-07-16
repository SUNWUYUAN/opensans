<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>网页版sans启动器</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn href="https://github.com/SUNWUYUAN/opensans" target="_blank" text>
        <span class="mr-2">在GitHub上贡献</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <template>





        <v-row justify="center">
          <v-dialog v-model="dialog" persistent max-width="600">
            <template v-slot:activator="{ on, attrs }">
              <div class="fatherdiv">
                <div class="sondiv">
                  <v-btn color="primary" dark v-bind="attrs" v-on="on">
                    启动网页版sans模拟器
                  </v-btn>
                </div>
              </div>
            </template>


            <v-card>
              <v-toolbar color="primary" dark>启动网页版sans</v-toolbar>
              <div>
                <div style="height: 300px;overflow: auto;">
                  <v-btn class="ma-2" color="primary" href="url1  ">
                    sans1
                  </v-btn>  

                  <v-btn class="ma-2" color="primary" href="url2  ">
                    sans2
                  </v-btn>

                  <v-btn class="ma-2" color="primary" href="url3  ">
                    sans3
                  </v-btn>
                </div>
              </div>
              <v-card-actions class="justify-end">
                <v-btn color="primary" text @click="dialog = false">
                  取消
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>


      </template>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    }
  },
}
</script>

<style>
.fatherdiv {

  width: max-content;
  height: max-content;
}

.sondiv {

  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>
