<template>
  <div class="hello">
      <!-- Update or Create Product Review -->
      <div v-if="createBoolean">
        <transition name="modal">
          <div class="modal-mask">
            <div class="modal-wrapper">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" v-if="reviewTypeDetail === 'add'">Add Review for {{productData.name}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true" @click="close()">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <div class="container-fluid">
                      <div class="row invent-form">
                        <div class="col-6 br-1 p-50">
                          <div class="mb-30">
                            <label>NAME<sup class="err">*</sup></label>
                            <Input v-model="name" :maxlength="50" show-word-limit placeholder="Enter Name" style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.name}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>Date Of Birth<sup class="err">*</sup></label>
                            <DatePicker type="date" v-model="date_of_birth" :start-date="new Date(1960, 4, 14)" placeholder="Select date" style="width: 200px"></DatePicker>
                            <transition name="fade">
                              <div class="err">{{errorpayload.date_of_birth}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>Email Address<sup class="err">*</sup></label>
                            <Input v-model="email" type="email" :maxlength="50" show-word-limit placeholder="Enter Name" style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.email}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>Country<sup class="err">*</sup></label>
                            <Select v-model="country" filterable>
                              <Option v-for="item in countryList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                            </Select>
                            <transition name="fade">
                              <div class="err">{{errorpayload.country}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>City<sup class="err">*</sup></label>
                            <Select v-model="city" filterable>
                              <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
                            </Select>
                            <transition name="fade">
                              <div class="err">{{errorpayload.city}}</div>
                            </transition>
                          </div>  
                        </div>
                        <div class="col-6 p-50">
                          <div class="mb-30"><br>
                            <label>Things You Like</label><sup class="err">*</sup>
                            <Input v-model="likes" :maxlength="1440" show-word-limit type="textarea"
                             placeholder="Enter Things you like..." style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.likes}}</div>
                            </transition>
                          </div>
                          <div class="mb-30"><br>
                            <label>Things You Dislike</label><sup class="err">*</sup>
                            <Input v-model="dislikes" :maxlength="1440" show-word-limit type="textarea"
                             placeholder="Enter Things you dislike..." style="width: 200px" />
                            <transition name="fade">
                              <div class="err">{{errorpayload.dislikes}}</div>
                            </transition>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="close()">Close</button>
                    <button type="button" class="btn btn-primary" v-if="reviewType === 'add'" @click="createProductReview">SAVE</button>
                    <button type="button" class="btn btn-primary" v-if="reviewType === 'update'" @click="updateProductReview">Update</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>
      </div>
  </div>
</template>

<script src="./AddProductReview.js"></script>
<style src="./AddProductReview-styl.styl" lang="stylus" scoped></style>
