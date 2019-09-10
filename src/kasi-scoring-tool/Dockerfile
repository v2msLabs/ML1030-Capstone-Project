FROM node:12.2.0

# set up angular cli
#RUN yarn global add @angular/cli@8.2.1
#npm install -g @angular/cli@8.2.1
#RUN npm install -g @angular/cli

#RUN npm install
WORKDIR /app

# install and cache app dependencies
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm install
RUN npm install -g @angular/cli@8.2.1


#COPY yarn.lock /app
#RUN yarn install --pure-lockfile
COPY . /app

# create watch files
CMD ng serve --host 0.0.0.0 --disable-host-check --proxy-config proxy.conf.json
#CMD ng serve --host 0.0.0.0
EXPOSE 4200
