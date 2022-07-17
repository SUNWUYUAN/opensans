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
                  <v-btn class="ma-2" color="primary" href="http://jcw87.github.io/c2-sans-fight/">Sans</v-btn><v-btn class="ma-2" color="primary" href="https://mario1d240.github.io/error-sans-fight-demo/">Error 404 Sans</v-btn><v-btn class="ma-2" color="primary" href="https://meekuzo.github.io/Jotaro-Sans-Simulator/">Jotaro Sans(空条衫太郎)</v-btn><v-btn class="ma-2" color="primary" href="https://deleeeee.itch.io/undertalehard-mode-sans-fight-normal">Hard Mode Sans</v-btn><v-btn class="ma-2" color="primary" href="https://iknifeu.itch.io/underfell-sans-fight">Fell Sans</v-btn><v-btn class="ma-2" color="primary" href="https://fuck-time.github.io/CJ-bad-time-simulator/">Hard Mode Sans</v-btn><v-btn class="ma-2" color="primary" href="https://hyzq.github.io/Bee-Sans-fight3/">蜜蜂Sans</v-btn><v-btn class="ma-2" color="primary" href="https://deleeeee.itch.io/del-sans-fight-demo">DEL_Sans</v-btn><v-btn class="ma-2" color="primary" href="https://tjasbsdsbfhdf.itch.io/55555">NK!Sans(究极削弱)</v-btn><v-btn class="ma-2" color="primary" href="https://1742137113.github.io/haogesans/">Haoge Sans</v-btn>
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
