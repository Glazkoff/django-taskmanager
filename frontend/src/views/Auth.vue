<template>
  <v-app>
    <v-main>
      <v-container fill-height="fill-height">
        <v-row>
          <v-col
            col="12"
            sm="12"
            offset-sm="0"
            md="6"
            offset-md="3"
            lg="4"
            offset-lg="4"
          >
            <router-view></router-view>
          </v-col>
        </v-row>
        <!-- <v-layout align-center="align-center" justify-center="justify-center">
          <router-view></router-view>
        </v-layout> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Auth"
};
</script>

<style lang="scss" scoped></style>
